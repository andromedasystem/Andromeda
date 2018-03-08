import React from 'react';

class Text extends React.Component {
    render() {
        return <div>
                <p>This is a {this.props.test} using react-django serve-rendering</p>

        </div>
    }
}

export default Text;
