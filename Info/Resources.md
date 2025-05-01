## 1. Официальные ресурсы

[***ATP/WTA сайты***](): Полные данные по игрокам, результатам матчей, head-to-head статистике.

Турнирные порталы (например, Australian Open, Roland Garros): Детализация по сетам, покрытиям, историческим результатам.

## 2. Специализированные базы

[Tennis-Data.co.uk](http://tennis-data.co.uk/): Бесплатные CSV/Excel файлы с матчами с 2000-х годов.

[OnCourt](): Платный архив с расширенной статистикой и длительным охватом.

[Tennis Abstract](https://tennisabstract.com/) / [Tennis Abstract GitHub](https://github.com/JeffSackmann/tennis_atp): Аналитика + Match Charting Project (детализация каждого удара с 1968 года).

## 3. Аналитические платформы

[Tennisexplorer.com](https://www.tennisexplorer.com/): Статистика по покрытиям, W/L-показатели, динамика рейтингов.

[Tennisinsight](https://tennisinsight.com/): Прогнозы на основе формы игроков и травм.

[Matchstat](https://matchstat.com/): Углублённая подача/приём метрик.

## 4. Live-трекинг

[Sofascore](https://www.sofascore.com/tennis): Графики силы игроков, эйсы, двойные ошибки в реальном времени.

[Livesport](https://www.livesport.com/ru/tennis/).com: Архивные результаты + текущие матчи с детализацией по геймам.

Для ML-моделей актуально парсить Flashscore (статистика по очкам) или использовать HawkEye-данные (недоступны публично, требуют лицензии ATP). Для беттинга Nb-bet.com даёт предиктивные сводки по исходам.

Лайфхак: Для анализа Н2Н на конкретных покрытиях комбинируйте данные ATP с ручным парсингом Tennisexplorer



Реальные данные с TennisAbstract через парсинг (см. функцию get_player_stats выше).

Live-фичи через API Bet365/Sofascore.

Ансамблирование с XGBoost и LightGBM.