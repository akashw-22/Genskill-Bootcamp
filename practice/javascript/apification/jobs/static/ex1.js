'use strict';

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };	//this is the react component, state is an object to which 
    								//we pass the json object, liked which has value false now
  }

  render() {
    if (this.state.liked) {
    console.log("nalla thayli");
     
     return( <button onClick={ () => this.setState({liked : false }) }>
     			ninakk andi illa thirich povan ivde oomb
     			</button>);
     
     
     /* return React.createElement(
      		'button',
      		{ onClick : () => this.setState({ liked : false }) },
      	
      	'ninakk andi illa thirich poovan ivde oomb');
      */		
    }
    
    
      return React.createElement(
          'button',
          { onClick: () => this.setState({ liked: true }) },	//create function and set it to
          														//onCLICK
          'andi inde ivde thod poori'
      );
  }
}

const rdemo = document.querySelector("#rdemo");				//inside the div class rdemo this is
															//being  rendered
ReactDOM.render(React.createElement(LikeButton), rdemo);	//create and put in rdemo

