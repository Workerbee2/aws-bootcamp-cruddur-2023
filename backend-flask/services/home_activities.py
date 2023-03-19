from datetime import datetime, timedelta, timezone
#Honeycomb Creating a trace 
from opentelemetry import trace

# CloudWatch Logs ----
import logging

from lib.db import pool, query_wrap_array
#Honeycomb Creating a trace
tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run():
    #Cloudwatch logs
    #logger.info("HomeActivities") #turned off to save on spend
    #Honeycomb Creating a trace
    with tracer.start_as_current_span("home-activites-mock-data"):
      #span
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      #span
      span.set_attribute("app.now", now.isoformat())

    sql = query_wrap_array("""
SELECT
        activities.uuid,
        users.display_name,
        users.handle,
        activities.message,
        activities.replies_count,
        activities.reposts_count,
        activities.likes_count,
        activities.reply_to_activity_uuid,
        activities.expires_at,
        activities.created_at
      FROM public.activities
      LEFT JOIN public.users ON users.uuid = activities.user_uuid
      ORDER BY activities.created_at DESC    """)
    print("SQL-------")
    print(sql)
    print("SQL________")


    with pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(sql)
        # this will return a tuple
        # the first field being the data
        json = cur.fetchone()
    print("-----")
    print(json[0])
    return json[0]
    #span.set_attributes("app.result_length", len(results))
    return results
