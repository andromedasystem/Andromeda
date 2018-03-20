import React, { Component } from 'react';
import { Icon, Menu, Dropdown } from 'semantic-ui-react';

class Nav extends Component {

    constructor(props){
        super(props);
        this.state = {
            is_admin: this.props.is_admin,
            is_ft_student: this.props.is_ft_student ,
            is_pt_student: this.props.is_pt_student,
            is_ft_faculty: this.props.is_ft_faculty,
            is_pt_faculty: this.props.is_pt_faculty,
            is_researcher: this.props.is_researcher,
            is_faculty: this.props.is_faculty
        }
    }


	render() {
        let menu;
        if(this.state.is_admin) {
            menu = <Dropdown.Menu>
                        <Dropdown.Item ><a style={{width: '100%', height: '100%', color: 'black'}} href="/student_system/create_course/">Create Course</a></Dropdown.Item>
                        <Dropdown.Item>Update Course</Dropdown.Item>
                        <Dropdown.Item>Create Section</Dropdown.Item>
                        <Dropdown.Item>Update Section</Dropdown.Item>
                    </Dropdown.Menu>;
        } else if(this.state.is_faculty) {
            menu = <Dropdown.Menu>
                    <Dropdown.Item><a href="/student_system/">Faculty Course Placeholder</a></Dropdown.Item>
            </Dropdown.Menu>;
        } else if(this.state.is_pt_student || this.state.is_ft_student){
            menu= <Dropdown.Menu>
                    <Dropdown.Item><a href="/student_system/">Register for a course</a></Dropdown.Item>
            </Dropdown.Menu>
        }

		return (
		    <Menu style={menuStyle} compact >
                <Dropdown simple item text='Course Actions'>
                    { menu }
                </Dropdown>
                <Dropdown simple item text='Student Actions'>
                    <Dropdown.Menu>
                        <Dropdown.Item>View/Update Hold</Dropdown.Item>
                        <Dropdown.Item>View Student Transcript</Dropdown.Item>
                        <Dropdown.Item>View Student Schedule</Dropdown.Item>
                    </Dropdown.Menu>
                </Dropdown>
                <Dropdown simple item text='Administrative Actions'>
                    <Dropdown.Menu>
                        <Dropdown.Item>Edit Permissions</Dropdown.Item>
                        <Dropdown.Item>Change Semester</Dropdown.Item>
                    </Dropdown.Menu>
                </Dropdown>
                <Dropdown simple item text='User Actions'>
                    <Dropdown.Menu>
                        <Dropdown.Item>Create User</Dropdown.Item>
                        <Dropdown.Item>Search/Update User</Dropdown.Item>
                   </Dropdown.Menu>
                </Dropdown>
            </Menu>

			);
	}
}

const menuStyle = {
    marginTop: '8rem'
};

export default Nav;