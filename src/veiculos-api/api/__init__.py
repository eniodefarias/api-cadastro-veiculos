from uvicorn import run as run_server

print("init7")


def main():
    print("init8")
    run_server("veiculos-api.api.app:app", worker=4, access_log=True, host="0.0.0.0")

# if __name__ == "__main__":
#     uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    print("init9")
    main()
