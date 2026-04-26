import requests
from django.http import JsonResponse
from django.conf import settings
from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)


def weather_view(request):
    district = request.GET.get('district')

    if not district or not district.isalpha():
        return JsonResponse(
            {'error': 'Valid district name is required'},
            status=400
        )

    api_key = settings.OPENWEATHER_API_KEY
    if not api_key:
        return JsonResponse(
            {'error': 'Server configuration error'},
            status=500
        )

    cache_key = f"weather_{district.lower()}"
    cached_data = cache.get(cache_key)

    if cached_data:
        return JsonResponse(cached_data)

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": f"{district},IN",
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        if response.status_code != 200:
            return JsonResponse(
                {'error': data.get('message', 'Failed to fetch weather')},
                status=response.status_code
            )

        result = {
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description']
        }

        cache.set(cache_key, result, timeout=600)

        return JsonResponse(result)

    except requests.Timeout:
        logger.error("Weather API timeout")
        return JsonResponse({'error': 'Request timed out'}, status=504)

    except requests.RequestException as e:
        logger.error(f"Weather API error: {str(e)}")
        return JsonResponse({'error': 'Failed to fetch weather data'}, status=500)

    except KeyError:
        logger.error("Invalid response structure")
        return JsonResponse({'error': 'Invalid data received'}, status=500)