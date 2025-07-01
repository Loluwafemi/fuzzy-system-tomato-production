


call .\app\fuzzy-env\Scripts\activate.bat


@echo off

setlocal

set "interfacex=C:\Program Files\fuzt\pake.exe"

if errorlevel 1 (
    echo "caught an expected exception"
    goto :catch
)

if exist "%interfacex%" (
    @REM pass and open interface
    echo "ui found"
    set "isready=1"

) else (
    @REM install the interface
    set "isready=0"
    echo "ui not found. intstalling..."
    start "" "./fuzt.msi"

)

if "%isready%" == "1" (
    @REM pass and open interface
    echo "ui found"
    start "" "C:\Program Files\fuzt\pake.exe"
) else (
    if not exist "%interfacex%" ( 
        set "isready=0" 
    )
)


goto :end

:catch
echo "Caught expected exception"

:end
endlocal


@echo on
python "./app/app.py"

pause
