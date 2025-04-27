
style = {
    'backgroundColor': 'black',
    'color': 'white',
    'margin': 0,
    "width": "100%",
    "border": 0
}



layoutStyle = {
    'backgroundColor': '#3c6454',
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



centerGridStyle = {
    
}
# __all__ = ["style"]