import os
import apache_beam as beam
from utils.pardo import BallsDontLie
from utils.method import json_to_csv_line

with beam.Pipeline() as pipeline:
    start = (
        pipeline
        | "Trigger Pipeline" >> beam.Create([
            {"url": os.getenv("URL")}
        ])
        | "Api Requisition from players" >> beam.ParDo(BallsDontLie())
        | "JSON to csv" >> beam.Map(json_to_csv_line)
        | "Write pages in a folder" >> beam.io.WriteToText("balls_dont_lie", header="id,first_name,height_feet,height_inches,last_name,position,team_id,team_abbreviation,team_city,team_conference,team_division,team_full_name,team_name")
    )
