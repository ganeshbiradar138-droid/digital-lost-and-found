from pymongo import MongoClient

print("Starting safe database migration...")
client = MongoClient("mongodb://localhost:27017/")

old_db_name = "lost_found "
new_db_name = "lost_found"

old_db = client[old_db_name]
new_db = client[new_db_name]

collections = old_db.list_collection_names()

if not collections:
    print(f"No data found in the old database '{old_db_name}'. Nothing to migrate.")
else:
    for old_col_name in collections:
        new_col_name = old_col_name.strip()
        old_col = old_db[old_col_name]
        new_col = new_db[new_col_name]

        if new_col.count_documents({}) > 0:
            print(f"Skipping '{old_col_name}' -> '{new_col_name}' (Target already has data).")
            continue

        docs = list(old_col.find())
        if docs:
            new_col.insert_many(docs)
            print(f"Migrated {len(docs)} documents from '{old_col_name}' to '{new_col_name}'.")
        else:
            print(f"No data in '{old_col_name}'.")

print("\nMigration complete. Verify the application before dropping the old database.")
