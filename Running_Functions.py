# Calculation of velocity returned as a number
# Distance needs to be entered as an int and time 'mm:ss.ms'
class Running_Func:
    def __init__(self, distance, time, mi=False):
        if mi == False:
            self.distance = distance
        else:
            self.distance = distance * 1600
        self.time = time

    def _total_sec(self):
        time_list = self.time.split(':')
        time_list.reverse()

        seconds = 0
        i = 0
        for item in time_list:
            if i == 0:
                seconds = seconds + float(item)
                i += 1
            elif i == 1:
                seconds = seconds + (float(item) * 60)
                i += 1
            else:
                seconds = seconds + (float(item) * 60 * 60)
                i += 1
        return seconds

    def _sec_to_time(self,total_sec):
        pace_min = round(total_sec // 60)
        pace_sec = round(((total_sec / 60) - pace_min) * 60, 2)
        if pace_sec < 10:
            pace_sec = f'0{pace_sec}'
        return (f'{pace_min}:{pace_sec}')

    def velocity_calc(self):
        return self.distance/self._total_sec()

    def pace(self):
        velocity = self.velocity_calc()
        sec_per_meter = 1/velocity
        sec_per_mile = sec_per_meter * 1609
        return self._sec_to_time(sec_per_mile)

    def velocity_percent(self, intensity):
        return self.velocity_calc() * intensity

    def pace_calc(self, intensity, intervals):
        velocity = self.velocity_calc() * intensity
        sec_per_meter = 1 / (velocity)
        sec_per_interval = sec_per_meter * intervals
        return self._sec_to_time(sec_per_interval)

    def race_intervals(self, interval):
        section_time = []
        velocity = self.velocity_calc()
        sec_per_meter = 1 / velocity
        section = interval
        while section < self.distance:
            sec_per_interval = sec_per_meter * section
            section_time.append([section, self._sec_to_time(sec_per_interval)])
            section += interval
        sec_per_interval = sec_per_meter * self.distance
        section_time.append([section, self._sec_to_time(sec_per_interval)])
        return section_time
