import React from 'react';

class Text extends React.Component {
    render() {
        return <div>
                <h1>This is a {this.props.test}</h1>
                <p>Hello World!</p>
        </div>
    }
}

export default Text;
