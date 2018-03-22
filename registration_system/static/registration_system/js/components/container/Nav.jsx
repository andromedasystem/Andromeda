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
            menu = <Menu style={menuStyle} compact>
                    <Dropdown simple item text='Course Actions'>
                        <Dropdown.Menu>
                            <Dropdown.Item ><a style={{width: '100%', height: '100%', color: 'black'}} href="/student_system/create_course/">Create Course</a></Dropdown.Item>
                            <Dropdown.Item><a style={{width: '100%', height: '100%', color: 'black'}} href="/student_system/search_course/">Update Course</a></Dropdown.Item>
                            <Dropdown.Item><a style={{width: '100%', height: '100%', color: 'black'}} href="/student_system/create_section/">Create Section</a></Dropdown.Item>
                            <Dropdown.Item><a style={{width: '100%', height: '100%', color: 'black'}} href="/student_system/search_section/">Update Section</a></Dropdown.Item>
                        </Dropdown.Menu>
                    </Dropdown>
                    <Dropdown simple item text='Student Actions'>
                    <Dropdown.Menu>
                        <Dropdown.Item><a style={{width: '100%', height: '100%', color: 'black'}} href="/student_system/create_hold/">Create Hold</a></Dropdown.Item>
                        <Dropdown.Item><a style={{width: '100%', height: '100%', color: 'black'}} href="/student_system/create_advising/">Create Advising</a></Dropdown.Item>
                        <Dropdown.Item>View Student Transcript</Dropdown.Item>
                        <Dropdown.Item>View Student Schedule</Dropdown.Item>
                    </Dropdown.Menu>
                </Dropdown>
                <Dropdown simple item text='Administrative Actions'>
                    <Dropdown.Menu>
                        <Dropdown.Item><a style={{width: '100%', height: '100%', color: 'black'}} href="/student_system/change_semester/">Change Semester</a></Dropdown.Item>
                    </Dropdown.Menu>
                </Dropdown>
                <Dropdown simple item text='User Actions'>
                    <Dropdown.Menu>
                        <Dropdown.Item><a style={{width: '100%', height: '100%', color: 'black'}} href="/student_system/create_user/">Create User</a></Dropdown.Item>
                        <Dropdown.Item><a style={{width: '100%', height: '100%', color: 'black'}} href="/student_system/search_user/">Search/Update User</a></Dropdown.Item>
                   </Dropdown.Menu>
                </Dropdown>
            </Menu>;
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
		    <div>
            { menu }
            </div>
			);
	}
}

const menuStyle = {
    marginTop: '8rem'
};

export default Nav;