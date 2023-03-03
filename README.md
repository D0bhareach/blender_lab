#### 1. Реализовать автоматическое тестирование Blender 3.X.
   [Blender 3.3]( https://www.blender.org/download/releases/3-3/)   
   Необходимо разработать программу, которая будет проверять работу Blender, исполняя
   несколько сценариев. Примеры:
1. Создание произвольных фигур без материала.
2. Создание произвольных фигур с материалом с различными параметрами.
3. Использование различного освещение со сценариями из Пункта 2.
   На вход ожидаются аргументы:
   * blender_path – путь до исполняемого файла blender.exe
   * output_path – папка в которую будут сохраняться результаты тестирования.
   * x_resolution – ширина отрендеренного изображения.
   * y_resolution – высота отрендеренного изображения.

   На выходе ожидаются:
   * Отрендеренное изображение для каждого сценария
   * Лог рендера для каждого сценария.
   * JSON файл для каждого сценария, в котором будет:
      * Название теста (произвольное).
      * Дата и время запуска теста.
      * Дата и время окончания теста.
      * Длительность теста.
      * Информация о системе (CPU, RAM, название операционной системы).
   

   Необходимо самостоятельно продумать структуру проекта, реализацию тестов, а также быть
   готовым продемонстрировать и объяснить решение. Результаты работы необходимо
   опубликовать в публичном репозитории на GitHub и прислать ссылку.  
   Полезные ссылки:  
   [blender manual](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html)   
   [blender api](https://docs.blender.org/api/latest/)      
    
    
    
#### Реализовать Jenkins Pipeline Job
   Необходимо реализовать Jenkins Pipeline Job, которая будет принимать параметры из задания 1,
   выполнять сценарии на подключенном узле и сохранять все выходные файлы в качестве
   артефактов.
   Шаги для выполнения:
   * Установить Jenkins локально
   * Подключить Jenkins node (локально)
   * Создать Job -> Pipeline
   * Сконфигурировать данный проект
     * Разработать Pipeline на языке Groovy, который будет выполнять следующие
     действия:
     * Получение x_resolution и y_resolution в качестве входных параметром.
     * Выбор нужно узла для выполнения кода.  
     * Выкачивание проекта с тестами из GitHub.  
     * Запуск тестов с переданными x_resolution и y_resolution  
     * Сохранение файлов, являющихся результатами тестирования, в качестве  
     артефактов запуска.    
     Исходный код Pipeline необходимо опубликовать в публичном репозитории на GitHub и прислать
     ссылку.    
     

Полезные ссылки:  
https://www.jenkins.io/doc/book/installing/  
https://www.jenkins.io/doc/book/pipeline/  
https://www.jenkins.io/doc/book/using/using-agents/   