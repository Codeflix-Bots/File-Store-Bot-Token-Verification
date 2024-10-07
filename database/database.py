#Don't remove This Line From Here. Tg: @sewxiy | @Codeflix_Bots
import time
import pymongo, os
from config import DB_URI, DB_NAME
from bot import Bot


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]


user_data = database['users']
collection = database['premium-users']

default_verify = {
    'is_verified': False,
    'verified_time': 0,
    'verify_token': "",
    'link': ""
}

def new_user(id):
    return {
        '_id': id,
        'verify_status': {
            'is_verified': False,
            'verified_time': "",
            'verify_token': "",
            'link': ""
        }
    }


async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user = new_user(user_id)
    user_data.insert_one(user)
    return

async def db_verify_status(user_id):
    user = user_data.find_one({'_id': user_id})
    if user:
        return user.get('verify_status', default_verify)
    return default_verify

async def db_update_verify_status(user_id, verify):
    user_data.update_one({'_id': user_id}, {'$set': {'verify_status': verify}})

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return

async def add_premium(user_id, time_limit_months):
    expiration_timestamp = int(time.time()) + time_limit_months * 30 * 24 * 60 * 60
    premium_data = {
        "user_id": user_id,
        "expiration_timestamp": expiration_timestamp,
    }
    collection.insert_one(premium_data)
    dbclient.close()

async def remove_premium(user_id):
    result = collection.delete_one({"user_id": user_id})
    dbclient.close()

async def remove_expired_users():
    current_timestamp = int(time.time())

    # Find and delete expired users
    expired_users = collection.find({"expiration_timestamp": {"$lte": current_timestamp}})
    
    for expired_user in expired_users:
        user_id = expired_user["user_id"]
        collection.delete_one({"user_id": user_id})

    dbclient.close()

async def list_premium_users():

    premium_users = collection.find({})
    
    premium_user_list = []

    for user in premium_users:
        user_id = user["user_id"]
        user_info = Bot.get_users(user_id)
        username = user_info.username if user_info.username else user_info.first_name
        expiration_timestamp = user["expiration_timestamp"]
        premium_user_list.append(f"{user_id} - {username} - Expiration Timestamp: {expiration_timestamp}")

    return premium_user_list
