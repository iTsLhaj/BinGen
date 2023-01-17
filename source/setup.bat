@echo off

echo:

cls

::: TODO: SET A GREEN COLOR HH

:::             *     ,MMM8&&&.            *
:::                  MMMM88&&&&&    .
:::                 MMMM88&&&&&&&
:::     *           MMM88&&&&&&&&
:::                 MMM88&&&&&&&&
:::                 'MMM88&&&&&&'
:::                   'MMM8&&&'      *
:::          |\___/|
:::          )     (             .              '
:::         =\     /=
:::           )===(       *
:::          /     \
:::          |     |    
:::         /       \
:::         \       /
:::  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_
:::  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |  |  |
:::  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |  |  |
:::  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |  |  |
:::  |  |  |  |  |  |  |  |  |  |  |  | by: iTsLhaj  |
:::  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do @echo(%%A

echo:

set levels_=NOTSET INFO DEBUG ERROR
echo Set a logging level or leave it blank ( sets to INFO by defdault when leaving it blank )
set /p LOGGING_LEVEL= - Set a logging level (NOTSET/INFO/DEBUG/ERROR): 

if "%LOGGING_LEVEL%"=="" set LOGGING_LEVEL=INFO

(for %%a in (%levels_%) do (
    if %%a == %LOGGING_LEVEL% (

        echo LoggingLevel: %LOGGING_LEVEL% > config.yaml
        echo config file created successfully
        timeout 3
        cls

        pip install -r requirements.txt
        cls
        echo SETUP DONE !
        timeout 3

        exit 0
    
    )
))

cls

echo - Level: %LOGGING_LEVEL% ? NOT IN LEVELS (NOTSET/INFO/DEBUG/ERROR)
echo - Level Will Be INFO u can change it from config.yaml file

echo LoggingLevel: %LOGGING_LEVEL% > config.yaml
echo config file created successfully

timeout 3

cls

::: TODO: RESET THE COLOR HH

exit 0