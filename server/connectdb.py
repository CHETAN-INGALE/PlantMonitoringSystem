import psycopg2

def insertSensorData(config, t, h, m):
    try:
        with psycopg2.connect(**config) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO plant_data (temp, humidity, moisture) VALUES (%s, %s, %s)", (t, h, m))
            conn.commit()
            print("Data inserted successfully!")
    except Exception as e:
        print(f"Error: {e}")

def lastTemp(config):
    try:
        with psycopg2.connect(**config) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT temp, date_time FROM public.plant_data ORDER BY date_time DESC LIMIT 1;")
            result = cursor.fetchone()
            t, dt = result[0], str(result[1])
            data = {
                "temp": t,
                "date_time": dt
            }
            return data
    except Exception as e:
        print(f"Error: {e}")
        
def lastHumidity(config):
    try:
        with psycopg2.connect(**config) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT humidity, date_time FROM public.plant_data ORDER BY date_time DESC LIMIT 1;")
            result = cursor.fetchone()
            h, dt = result[0], str(result[1])
            data = {
                "humidity": h,
                "date_time": dt
            }
            return data
    except Exception as e:
        print(f"Error: {e}")
        
def lastMoisture(config):
    try:
        with psycopg2.connect(**config) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT moisture, date_time FROM public.plant_data ORDER BY date_time DESC LIMIT 1;")
            result = cursor.fetchone()
            m, dt = result[0], str(result[1])
            data = {
                "moisture": m,
                "date_time": dt
            }
            return data
    except Exception as e:
        print(f"Error: {e}")
        
def lastSensorData(config):
    try:
        with psycopg2.connect(**config) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT temp, humidity, moisture, date_time FROM public.plant_data ORDER BY date_time DESC LIMIT 1;")
            result = cursor.fetchone()
            t, h, m, dt = result[0] ,result[1] ,result[2] , str(result[3])
            data = {
                "temp": t,
                "humidity": h,
                "moisture": m,
                "date_time": dt
            }
            return data
    except Exception as e:
        print(f"Error: {e}")