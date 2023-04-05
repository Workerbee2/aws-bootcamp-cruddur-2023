from datetime import datetime, timedelta, timezone
#Honeycomb Creating a trace 
from opentelemetry import trace

# CloudWatch Logs ----
import logging

#Postgresql
from lib.db import db

#Honeycomb Creating a trace
#tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run(cognito_user_id=None):
    #print("====home activities")
    #Cloudwatch logs
    #logger.info("HomeActivities") #turned off to save on spend
    #Honeycomb Creating a trace
      
    results = db.query_array_json("""
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
      ORDER BY activities.created_at DESC    
    """)
##    span.set_attributes("app.result_length", len(results))
    return results
