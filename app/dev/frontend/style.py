
style = {
    'backgroundColor': 'black',
    'color': 'white',
    'margin': 0,
    "width": "100%",
    "border": 0
}



layoutStyle = {
    'background': '#A60042',
    'background': 'linear-gradient(164deg,rgba(53, 70, 74, 1) 0%, rgba(123, 212, 160, 1) 50%, rgba(166, 0, 66, 1) 100%)',
    "display": "flex",
    "flexDirection": "row",
    "miWidth": "50%",
    "maxWidth": "100%",
    "height": "100vh",
    "justifyContent": "space-between"
}

centerComponentStyle = {
    'color': 'white',
    'margin': 0,
    "width": "100%",
    "height": "100vh",
    "overflowY": "scroll",
    "overflowX": "none",
    
}

sideComponentsStyles = {
    "display": "grid",
    "gridTemplateRows": "auto auto",
    'color': 'white',
    'margin': 0,
    "width": "40%",
    "alignContent": "space-between",
    "alignItems": "end",
    "overflowY": "scroll"

}


componentSectionStyle = {
        "border": "solid 1px white",
        "borderRadius": '4px',
        "height": "fit-content",
        "flexDirection": 'column',
        "margin": "4px",
        
        
}

standardWidget = {
    "display": "flex",
    "alignItems": 'center',
    "justifyContent": 'center',
    "border": "solid 1px white",
    "margin": "3px",
    "color": "white",
    'backgroundColor': 'transparent',
    "width": "auto",
    "height": "47vh",
}

standardTopWidget = {
    "display": "",
    "border": "solid 1px white",
    "margin": "3px",
    "color": "black",
    'backgroundColor': 'transparent',
    "width": "",
    "height": "50vh"
}



widgetLayout = {
    'autosize': True,
    "width": "0%",
    'backgroundColor': 'transparent',
    
    }

figureStyle = {
                'autosize': True,
                "height": "inherit",
                "width": "100%"
            }

sectionThreeStyle = {
    "display": "flex",
    "border": "solid 0px white",
    "height": "100vh",
    "flexDirection": "row"

}


tabsStyle = {

    "color": 'black',
    "margin": "4px"
}

tabChildrenStyle = {
    "color": 'white',
    "backgroundColor": "transparent",
}


defaultCardStyle = {
    "display": "flex", 
    "justifyContent": "center", 
    "alignItems": "center", 
    "height": "inherit", 
    "color": "white"
    }


# commonality

sectionThreeStyle.update(componentSectionStyle)


# onboard page

onboard = {
    "display": "grid",
    "gridTemplateColumns": "15% auto",
    "gap": "4px",
    "background-image": "url('/assets/img/fuzzy-assistance.jpg')",
    # "background-repeat": "no-repeat",
    "background-position": "center",
    "background-size": "contain",
    "width": "100%",
    "object-fit": "fill",
    "height": "100vh"
}

onboard_nav = {
    "display": "flex",
    "justifyContent": "space-around",
    "margin": "1px",
    # "border": "solid #102542 2px",
    "backgroundColor": "rgba(24, 23, 23, 0.41)",
    "borderRadius": "4px",
    "flexDirection": "column",
    "color": "white",
    "padding": "12px",
    "-webkit-backdrop-filter": "blur(5px)",
    "backdrop-filter": "blur(5px)"
}

onboard_nav_items = {
    # "height": "35vh",
    # "border": "solid grey 2px",
    "borderRadius": "3px"
}


onboard_section = {
    "margin": "1px",
    "border": "solid black 2px",
    "height": "100vh",
    "display": "flex",
    "align-items": "center",
    "justify-content": "center",
    "overflowY": "scroll",
    "backgroundColor": "rgba(43, 43, 43, 0.82)",
    "-webkit-backdrop-filter": "blur(5px)",
    "backdrop-filter": "blur(5px)"
}


onboard_content = {
    # "backgroundColor": "rgba(24, 23, 23, 0.65)",
    # "-webkit-backdrop-filter": "blur(5px)",
    # "backdrop-filter": "blur(5px)",
    "padding": "30px",
    "color": "white",
    # "border-radius": "5px",
    # "border": "2px solid white"

}

onboard_tab_styling = {
    "display": "flex",
    "flexDirection": "column"
}

onboard_tab_item_style = {
    "width": "auto",
    "margin": "1px",
    "color": "black"
}

tab_selected_style = {
    'borderTop': '1px solid #32E476',
    'borderBottom': '1px solid #32E476',
    'backgroundColor': 'black',
    'color': 'white',
    'padding': '6px',
    "width": "auto"
}