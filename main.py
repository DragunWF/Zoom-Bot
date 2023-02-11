from time import sleep
from scripts.bot import Bot
from scripts.time_getter import TimeGetter
from scripts.db_tool import DatabaseTool
from scripts.utils import Utils


def startup_greeting():
    year = TimeGetter.get_year()
    month = TimeGetter.get_month()
    day_of_month = TimeGetter.get_day_of_month()
    day_of_week = TimeGetter.get_day().capitalize()
    hour = Utils.format_hour(TimeGetter.get_hour())

    Utils.colored_print(f"{month} {day_of_month} {year} | {hour} {day_of_week}",
                        color="cyan")


def main():
    startup_greeting()
    db_tool = DatabaseTool()
    db_tool.insert_program_opened_record()
    bot = Bot(db_tool)
    bot.start_automation()


if __name__ == "__main__":
    main()
