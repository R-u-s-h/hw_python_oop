class InfoMessage:
    """Информационное сообщение о тренировке."""


class Training:
    """Базовый класс тренировки."""
    M_IN_KM = 1000
    LEN_STEP = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""


class Running(Training):
    """Тренировка: бег."""
    c_cal_01 = 18
    c_cal_02 = 20   

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories = ((self.c_cal_01 * self.get_mean_speed() 
                    - self.c_cal_02) * self.weight / self.M_IN_KM 
                    * self.duration * 60)
        return calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    c_cal_01 = 0.035
    c_cal_02 = 0.029

    def __init__(self, 
                 action: int, 
                 duration: float, 
                 weight: float, 
                 height: float
                 ) -> None:

        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories = ((self.c_cal_01 * self.weight 
                   + (self.get_mean_speed() ** 2 // self.height) 
                   * self.c_cal_02 * self.weight) * self.duration * 60)
        return calories


class Swimming(Training):
    """Тренировка: плавание."""
    c_cal_01 = 1.1
    c_cal_02 = 2
    
    def __init__(self, 
                action: int, 
                duration: float, 
                weight: float, 
                length_pool: float, 
                count_pool:float
                ) -> None:
        
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = (self.length_pool * self.count_pool / self.M_IN_KM 
                     / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories = ((self.get_mean_speed() + self.c_cal_01) 
                   * self.c_cal_02 * self.weight)
        return calories

class InfoMessage:
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
    
    def get_message() -> str:
        print(f'Тип тренировки: {training_type}; Длительность: {duration} ч.;' 
               'Дистанция: {distance} км; Ср. скорость: {speed} км/ч;'
               'Потрачено ккал: {calories}')
        

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
