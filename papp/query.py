from django.db import connection
from django.db import DatabaseError

def insert_data(phone_number, user_name):
    query = "INSERT INTO papp_master_user (user_m_no, user_name) VALUES (%s, %s)"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, [phone_number, user_name])

        connection.commit()
        print("Data inserted successfully!")
    except DatabaseError as e:
        print(f"Error occurred while inserting data: {str(e)}")

def update_otp_status(phone_number):
    result = ''
    query = " UPDATE papp_master_user SET otp_status = true WHERE user_m_no = %s;"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, [phone_number])

        result += 'True'
    except DatabaseError as e:
        result += 'False'
        print(f"Error occurred while inserting data: {str(e)}")

    return result


def get_user_name(phone_number):
    query = "SELECT pmu.user_name from papp_master_user pmu WHERE pmu.user_m_no = %s;"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, [phone_number])
            result = cursor.fetchone()  # Fetch the first row

        if result is not None:
            user_name = result[0]
            return user_name
        else:
            return None  

    except DatabaseError as e:
        print(f"Error occurred while retrieving data: {str(e)}")
        return None

def delete_user(phone_number):
    query = "DELETE from papp_master_user pmu WHERE pmu.user_m_no = %s;"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, [phone_number])
            print("data deleted")
    except DatabaseError as e:
        print(f"Error occurred while retrieving data: {str(e)}")


# SELECT img FROM papp_master_img;


def get_all_images():
    query = "SELECT img, img_name FROM papp_master_img;"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()

        images = [{'img': row[0], 'img_name': row[1]} for row in results]
        return images

    except Exception as e:
        print(f"Error occurred while retrieving images: {str(e)}")
        return []


def insert_transaction(user_id, img_id, response):
    query = "INSERT INTO papp_master_transactions (user_id, img_id, status) VALUES (%s, %s, %s);"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, [user_id, img_id, response])

        connection.commit()
        print("Data inserted successfully!")
    except DatabaseError as e:
        print(f"Error occurred while inserting data: {str(e)}")


def get_user_id(user_name):
    query = "SELECT pmu.id FROM papp_master_user pmu WHERE user_name = %s;"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, [user_name])
            result = cursor.fetchone()  # Fetch the first row

        if result is not None:
            user_name = result[0]
            print(user_name)
            return user_name
        else:
            return None  

    except DatabaseError as e:
        print(f"Error occurred while retrieving data: {str(e)}")
        return None


def get_img_id(img_name):
    query = "SELECT pmi.id FROM papp_master_img pmi WHERE img_name = %s;"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, [img_name])
            result = cursor.fetchone()  # Fetch the first row

        if result is not None:
            img_name = result[0]
            print(img_name)
            return img_name
        else:
            return None  

    except DatabaseError as e:
        print(f"Error occurred while retrieving data: {str(e)}")
        return None

def get_image_data(user_id):
    query = "SELECT pmt.img_id, pmt.status FROM papp_master_transactions pmt WHERE user_id = %s;"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, [user_id])
            results = cursor.fetchall()

        image_data = [{'img_id': row[0], 'status': row[1]} for row in results]
        print(image_data, "bhaiiiiiiiiii")
        return image_data

    except Exception as e:
        print(f"Error occurred while retrieving images: {str(e)}")
        return []