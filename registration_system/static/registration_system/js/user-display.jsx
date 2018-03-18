import React from 'react';
import Nav from './components/container/Nav.jsx';

class Index extends React.Component {

    constructor(props){
        super(props);
    }

    render() {
        return <div className="m-top8">
                <Nav
                    is_admin={this.props.is_admin}
                    is_ft_student={this.props.is_full_time_student}
                    is_pt_student={this.props.is_part_time_student}
                    is_researcher={this.props.is_researcher}
                    is_ft_faculty={this.props.is_full_time_faculty}
                    is_pt_faculty={this.props.is_part_time_faculty}
                    is_faculty={this.props.is_faculty}/>

                {/*<DropdownExampleSelection/>*/}
                <h3 className="ui center aligned header"> Welcome {this.props.first_name} {this.props.last_name}</h3>
                <p><strong>UserName: </strong>{this.props.username}</p>
                <p><strong>First Name: </strong>{this.props.first_name}</p>
                <p><strong>Last Name: </strong>{this.props.last_name}</p>
                <p><strong>Email: </strong>{this.props.email}</p>
                <p>{this.props.is_admin && 'ia admin'}</p>
                <p>{this.props.is_full_time_student && 'is ft student'}</p>
                <p>{this.props.is_part_time_student && 'is pt student'}</p>
                <p>{this.props.is_full_time_faculty && 'is ft faculty'}</p>
                <p>{this.props.is_part_time_faculty && 'is pt faculty'}</p>
                <p>{this.props.is_researcher && 'is researcher'}</p>
            </div>
    }
}

export default Index;
