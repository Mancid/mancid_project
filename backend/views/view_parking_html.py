from jinja2 import Template
from apscheduler.schedulers.background import BackgroundScheduler
from backend.database.db_mongo import result_database
from backend.database.db_mongo import connect_db, main


ROUTE = "/parking"


def view():
  """
  This function return parkings in jinja2 in the front
  """
  parkings = result_database(connect_db())
  with open("front/parking.html") as file_:
    template = Template(file_.read())
    result = template.render(parkings=parkings)
  return result


sched = BackgroundScheduler(daemon=True)
sched.add_job(main,'interval',seconds=59)
sched.start()
main()
