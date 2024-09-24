# Eine Klasse für sich (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/classes/001/)
import calendar
import datetime


class Birthday:
  def __init__(self, day: int, month: int, year: int):
    self.day = day
    self.month = month
    self.year = year

  def days_until_next_birthday(self) -> int:
    now = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    this_year = self.build_datetime_leap_year_safe(now.year)
    if now <= this_year:
      return (this_year - now).days
    else:
      return (self.build_datetime_leap_year_safe(now.year + 1) - now).days

  def build_datetime_leap_year_safe(self, year: int):
    if self.month != 2 or self.day != 29 or calendar.isleap(year):
      return datetime.datetime(year, self.month, self.day)
    else:
      return datetime.datetime(year, self.month, self.day - 1)

  def __str__(self) -> str:
    return self.build_datetime_leap_year_safe(self.year).strftime('%d %B %Y')


def main():
  leap_year_birthday = Birthday(29, 2, 2000)

  print(Birthday(1, 3, 1999))
  print(leap_year_birthday)
  print(f'Days remaining until next birthday: {leap_year_birthday.days_until_next_birthday()}')


if __name__ == '__main__':
  main()