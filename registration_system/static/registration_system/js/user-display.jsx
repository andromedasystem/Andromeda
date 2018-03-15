import React from 'react';

class Index extends React.Component {



    render() {
        return <div className="m-top6">
                <h3 className="ui center aligned header"> User Information:</h3>
            <p><strong>UserName: </strong>{this.props.username}</p>
            <p><strong>First Name: </strong>{this.props.first_name}</p>
            <p><strong>Last Name: </strong>{this.props.last_name}</p>
            <p><strong>Email: </strong>{this.props.email}</p>
            <p>{this.props.is_admin && 'ia admin'}</p>
            <p>{this.props.is_full_time_student && 'is ft student'}</p>
            <p>{this.props.is_part_time_student && 'is pt student'}</p>
            <p>{this.props.is_researcher && 'is researcher'}</p>
            </div>
    }
}

export default Index;
