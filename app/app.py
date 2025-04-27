from dev.frontend.pages.dashboard import dashboard
from dev.frontend.pages.onboarding import onboarding



# render first page here
if __name__ == '__main__':
    dashboard.run(debug=True, dev_tools_hot_reload=True, dev_tools_hot_reload_interval=True, dev_tools_ui=False)
    # dashboard.run_server(debug=True)
    # dashboard


