from django.shortcuts import render

def index(request):
    template_name = "core/index.html"
    context = {}
    return render(request, template_name, context)


def services(request):
    template_name = "core/services.html"
    context = {
        'title': 'Our Services',
        'description': 'Comprehensive technology solutions from AthenaNG Consulting'
    }
    return render(request, template_name, context)


def our_team(request):
    template_name = "core/our-team.html"
    context = {
        'title': 'Our Team',
        'description': 'Meet our experienced team of technology industry veterans with decades of combined expertise.'
    }
    return render(request, template_name, context)


def vision_mission(request):
    template_name = "core/vision-mission.html"
    context = {
        'title': 'Vision & Mission',
        'description': 'Our vision and mission to enhance network quality with innovative, reliable, cost-effective solutions.'
    }
    return render(request, template_name, context)


def our_approach(request):
    template_name = "core/our-approach.html"
    context = {
        'title': 'Our Approach',
        'description': 'How we deliver technology solutions through quality, innovation, and experienced teams.'
    }
    return render(request, template_name, context)


def contact_us(request):
    template_name = "core/contact-us.html"
    context = {
        'title': 'Contact Us',
        'description': 'Get in touch with AthenaNG Consulting for cutting-edge technology solutions and support.'
    }
    return render(request, template_name, context)

def service_details(request, service_slug):
    # Map service slugs to template names and data
    services_data = {
        'network-design': {
            'template': 'core/service-details.html',
            'title': 'Network Design & Optimization',
            'description': 'Global network engineering solutions for optimal performance',
            'icon': 'bi-diagram-3',
            'data': {
                'hero_title': 'Network Design & Optimization',
                'hero_description': 'AthenaNG Consulting Ltd. is a global name in the network engineering field and has designed several networks worldwide.',
                'overview': 'With over 7 decades of combined expertise, we have built a very strong brand with global footprint in the network engineering field and the technology industry in general. Our team of professionals are technology industry veterans, haven worked for Fortune 100 Telecom industry leaders with vast experience in multiple disciples.',
                'full_description': '''
                    <p>As our clients business requirements evolve, we are also challenged daily to improve on our performance to support their operations with high-speed network design and optimization solutions that connect their teams and improve productivity.</p>
                    
                    <p>AthenaNg leverages advanced technologies and high-speed networking to reach every corner of your operations, securely and reliably. We simply go beyond the fundamentals to develop strategically robust and responsive networks for your organization.</p>
                ''',
                'features': [
                    {
                        'title': 'Global Network Architecture',
                        'description': 'Design networks that span continents with optimal connectivity and performance.',
                        'icon': 'bi-globe'
                    },
                    {
                        'title': 'Performance Optimization',
                        'description': 'Enhance network speed, reliability, and efficiency through advanced optimization techniques.',
                        'icon': 'bi-speedometer2'
                    },
                    {
                        'title': 'Scalable Solutions',
                        'description': 'Design networks that grow with your business, ensuring long-term viability and cost-effectiveness.',
                        'icon': 'bi-arrow-up-right'
                    },
                    {
                        'title': 'Security Integration',
                        'description': 'Build security into the network architecture from the ground up for comprehensive protection.',
                        'icon': 'bi-shield-check'
                    }
                ],
                'benefits': [
                    'Improved network performance and reliability',
                    'Reduced total cost of ownership',
                    'Enhanced user experience and productivity',
                    'Scalable architecture for future growth',
                    'Integrated security measures',
                    'Global implementation expertise'
                ],
                'process': [
                    {
                        'step': 1,
                        'title': 'Needs Assessment',
                        'description': 'Analyze current infrastructure and business requirements'
                    },
                    {
                        'step': 2,
                        'title': 'Strategic Planning',
                        'description': 'Develop comprehensive network architecture designs'
                    },
                    {
                        'step': 3,
                        'title': 'Implementation',
                        'description': 'Deploy optimized network solutions with minimal disruption'
                    },
                    {
                        'step': 4,
                        'title': 'Optimization',
                        'description': 'Continuously monitor and enhance network performance'
                    }
                ],
                'technologies': [
                    'Cisco Systems',
                    'Juniper Networks',
                    'Arista Networks',
                    'Fortinet',
                    'Palo Alto Networks',
                    'SD-WAN Solutions'
                ],
                'stats': [
                    {
                        'value': '2000+',
                        'label': 'Networks Designed'
                    },
                    {
                        'value': '70+',
                        'label': 'Years Combined Expertise'
                    },
                    {
                        'value': '40%',
                        'label': 'Avg. Performance Improvement'
                    },
                    {
                        'value': 'Global',
                        'label': 'Implementation Footprint'
                    }
                ]
            }
        },
        'network-deployment': {
            'template': 'core/service-details.html',
            'title': 'Network Deployment & Roll-Out',
            'description': 'Professional network deployment and implementation services',
            'icon': 'bi-wifi',
            'data': {
                'hero_title': 'Network Deployment & Roll-Out',
                'hero_description': 'We undertake effective and professional Network Deployment and Roll-Out services covering planning, design, integration, optimization, fixed wireless access, end-to-end logistics management etc.',
                'overview': 'We understand that, when it comes to building new and fully deployed wireless networks efficiently or expanding an existing one, requires some amount of experience and deep insight into all areas of network planning, design, deployment, and optimization.',
                'full_description': '''
                    <p>Our Network Deployment and Roll-Out Services are delivered by professionals with a strong track record of deploying and installing Network solutions in line with best practice.</p>
                    
                    <p>At AthenaNg Consulting, we stay up to date with all current and upcoming telecommunication technologies and networks including fixed line networks, cellular telecommunications, wired and wireless broadband modes and optical technologies which we believe sets apart from the rest.</p>
                    
                    <p>AthenaNg Consulting can power a network, delivering 2G, 2.5G, 3G and beyond networks utilizing the best of local, in-house capabilities, subcontractors and central resources by leveraging effective team co-ordination, program management and project accountability to deploy advanced networks.</p>
                    
                    <p>At AthenaNg, we also provide post deployment services which includes 24/7 monitoring, L2/L3 technical assistance, issue fixing and escalation that enable process improvement and operational efficiency. In addition, to ensure the service availability, we also provides services like change management, network maintenance and other critical services.</p>
                ''',
                'features': [
                    {
                        'title': 'End-to-End Deployment',
                        'description': 'Complete network deployment from planning to post-deployment support.',
                        'icon': 'bi-check-circle'
                    },
                    {
                        'title': 'Multi-Technology Support',
                        'description': 'Expertise in 2G, 2.5G, 3G, 4G, 5G and beyond network technologies.',
                        'icon': 'bi-wifi'
                    },
                    {
                        'title': '24/7 Monitoring',
                        'description': 'Continuous monitoring and support after deployment for optimal performance.',
                        'icon': 'bi-eye'
                    },
                    {
                        'title': 'Logistics Management',
                        'description': 'Comprehensive project management and logistics coordination.',
                        'icon': 'bi-truck'
                    }
                ],
                'benefits': [
                    'Quick and efficient network deployment',
                    'Minimal business disruption during roll-out',
                    'Comprehensive post-deployment support',
                    'Expert handling of complex technologies',
                    'Scalable deployment strategies',
                    'Proven track record with Fortune 100 clients'
                ],
                'process': [
                    {
                        'step': 1,
                        'title': 'Planning & Design',
                        'description': 'Detailed planning and network architecture design'
                    },
                    {
                        'step': 2,
                        'title': 'Resource Allocation',
                        'description': 'Coordination of teams, equipment, and logistics'
                    },
                    {
                        'step': 3,
                        'title': 'Deployment Execution',
                        'description': 'Professional installation and configuration'
                    },
                    {
                        'step': 4,
                        'title': 'Testing & Support',
                        'description': 'Comprehensive testing and ongoing support'
                    }
                ],
                'technologies': [
                    'Cellular Networks (2G-5G)',
                    'Fixed Wireless Access',
                    'Fiber Optic Networks',
                    'Wireless Broadband',
                    'Optical Technologies',
                    'Network Monitoring Tools'
                ],
                'stats': [
                    {
                        'value': 'Global',
                        'label': 'Deployment Experience'
                    },
                    {
                        'value': '24/7',
                        'label': 'Monitoring Support'
                    },
                    {
                        'value': '100+',
                        'label': 'Successful Roll-Outs'
                    },
                    {
                        'value': 'Enterprise',
                        'label': 'Grade Solutions'
                    }
                ]
            }
        },
        'systems-integration': {
            'template': 'core/service-details.html',
            'title': 'Systems Integration',
            'description': 'Seamless integration of IT systems and applications',
            'icon': 'bi-hdd-network',
            'data': {
                'hero_title': 'Systems Integration',
                'hero_description': 'At AthenaNg Consulting, we aim at improving the quality of work and satisfaction of our customers by providing direct access to all the resources of the organization that helps to increased productivity.',
                'overview': 'When a company adopts a new technology or business process, they face many challenges between their current applications and systems and the complicated software implementation process.',
                'full_description': '''
                    <p>Our Systems Integration services connects various IT systems, hardware and software into one cohesive and well-functioning body.</p>
                    
                    <p>Our professional Engineers handle all of your challenging integration & implementation obstacles, including architectural design, testing, debugging, and execution.</p>
                    
                    <p>We specialize in creating seamless connections between diverse systems, ensuring they work together harmoniously to support your business operations and drive productivity.</p>
                ''',
                'features': [
                    {
                        'title': 'Architectural Design',
                        'description': 'Design robust integration architectures for complex IT environments.',
                        'icon': 'bi-diagram-3'
                    },
                    {
                        'title': 'API Integration',
                        'description': 'Expertise in RESTful APIs, SOAP, and custom integration protocols.',
                        'icon': 'bi-plug'
                    },
                    {
                        'title': 'Testing & Debugging',
                        'description': 'Comprehensive testing to ensure seamless system interoperability.',
                        'icon': 'bi-bug'
                    },
                    {
                        'title': 'Legacy System Integration',
                        'description': 'Integration of modern systems with existing legacy infrastructure.',
                        'icon': 'bi-arrow-left-right'
                    }
                ],
                'benefits': [
                    'Increased operational efficiency',
                    'Reduced system complexity',
                    'Improved data flow between systems',
                    'Enhanced user experience',
                    'Cost-effective integration solutions',
                    'Future-proof architecture design'
                ],
                'process': [
                    {
                        'step': 1,
                        'title': 'System Analysis',
                        'description': 'Assess current systems and integration requirements'
                    },
                    {
                        'step': 2,
                        'title': 'Integration Design',
                        'description': 'Create comprehensive integration architecture'
                    },
                    {
                        'step': 3,
                        'title': 'Development & Testing',
                        'description': 'Build and rigorously test integration solutions'
                    },
                    {
                        'step': 4,
                        'title': 'Deployment & Support',
                        'description': 'Implement integration and provide ongoing support'
                    }
                ],
                'technologies': [
                    'RESTful APIs',
                    'SOAP Web Services',
                    'Middleware Solutions',
                    'Enterprise Service Bus',
                    'Microservices Architecture',
                    'Cloud Integration'
                ],
                'stats': [
                    {
                        'value': '500+',
                        'label': 'Systems Integrated'
                    },
                    {
                        'value': '40%',
                        'label': 'Efficiency Improvement'
                    },
                    {
                        'value': 'Enterprise',
                        'label': 'Grade Solutions'
                    },
                    {
                        'value': '24/7',
                        'label': 'Support Available'
                    }
                ]
            }
        },
        'network-consulting': {
            'template': 'core/service-details.html',
            'title': 'Network Consulting & Transformation',
            'description': 'Strategic network consulting for digital transformation',
            'icon': 'bi-arrow-repeat',
            'data': {
                'hero_title': 'Network Consulting & Transformation',
                'hero_description': 'At AthenaNg, we believe your network is the platform for your digital transformation, and it needs to be flexible, robust and secure to adapt easily to business changes.',
                'overview': 'The IT industry is in the midst of its largest shift in history with the move to cloud, powered by the need to drive digital transformation initiatives now more topical than ever before.',
                'full_description': '''
                    <p>Our Network Consulting and Transformation Services along with professional System Integration, provide end-to-end solution to the constant difficulties most organization face on daily bases.</p>
                    
                    <p>Networks need to evolve to support the scale of data movement and processing. Our consulting services cover multiple dimensions, taking you on a complete journey from strategic discovery through to delivery of technologies and services with our Managed Service capability.</p>
                    
                    <p>We offer a high-touch, consultative approach where we work alongside our clients to build a blue-print for the network of the future. We tailor solutions for you with our technical capability in Networking, Datacentres, Cloud and Remote worker to deliver the branch of the future that todays' elastic workforce demands.</p>
                ''',
                'features': [
                    {
                        'title': 'Digital Transformation Strategy',
                        'description': 'Comprehensive roadmaps for network evolution and digital transformation.',
                        'icon': 'bi-lightbulb'
                    },
                    {
                        'title': 'Cloud Migration Planning',
                        'description': 'Expert guidance for migrating networks to cloud-based architectures.',
                        'icon': 'bi-cloud-arrow-up'
                    },
                    {
                        'title': 'Future-Proof Architecture',
                        'description': 'Design networks that adapt to evolving business needs and technologies.',
                        'icon': 'bi-building'
                    },
                    {
                        'title': 'Elastic Workforce Solutions',
                        'description': 'Network designs that support modern, distributed workforces.',
                        'icon': 'bi-people'
                    }
                ],
                'benefits': [
                    'Strategic network transformation planning',
                    'Reduced operational complexity',
                    'Enhanced business agility',
                    'Future-proof network architecture',
                    'Improved security posture',
                    'Optimized cloud integration'
                ],
                'process': [
                    {
                        'step': 1,
                        'title': 'Strategic Discovery',
                        'description': 'Assess current state and future business requirements'
                    },
                    {
                        'step': 2,
                        'title': 'Blueprint Development',
                        'description': 'Create comprehensive transformation roadmap'
                    },
                    {
                        'step': 3,
                        'title': 'Solution Design',
                        'description': 'Design tailored network transformation solutions'
                    },
                    {
                        'step': 4,
                        'title': 'Implementation Support',
                        'description': 'Guide and support transformation execution'
                    }
                ],
                'technologies': [
                    'Cloud Networking',
                    'SD-WAN Solutions',
                    'Zero Trust Architecture',
                    'Network Automation',
                    'Multi-Cloud Integration',
                    'IoT Infrastructure'
                ],
                'stats': [
                    {
                        'value': 'Strategic',
                        'label': 'Consulting Approach'
                    },
                    {
                        'value': 'Digital',
                        'label': 'Transformation Experts'
                    },
                    {
                        'value': 'Future-Proof',
                        'label': 'Architecture Design'
                    },
                    {
                        'value': 'Elastic',
                        'label': 'Workforce Solutions'
                    }
                ]
            }
        },
        'network-support': {
            'template': 'core/service-details.html',
            'title': 'Network Support & Staff Augmentation',
            'description': 'Comprehensive network support and IT staffing solutions',
            'icon': 'bi-people-fill',
            'data': {
                'hero_title': 'Network Support & Staff Augmentation',
                'hero_description': 'Is your organization short of the necessary skills to get your project delivered? then trust the technology experts to help fill the gap.',
                'overview': 'Whether remotely or in-house, our staff augmentation services provide the speed, expertise, and flexibility your team needs to scale up at any stage of the project and deliver on time for a specific period.',
                'full_description': '''
                    <p>Whatever type of assistance you require, we've got the staffing augmentation solution to get you where you need to go and provide the necessary network support just for you.</p>
                    
                    <p>This helps to reduce the cost of hiring for a fixed term and ensures to match you with experts who are the right fit for your business.</p>
                    
                    <h5>Augmentation Services Levels</h5>
                    <p>Our IT staff augmentation and network support services has been categorized into different levels based on their requirement in skills and experience. We start from Level 1 combined with level 2 support services to complement your Team's internal IT team's competencies.</p>
                    
                    <p><strong>Level 1:</strong> Our team members are ready to assist your internal customers (users) whether they are at the office or from remote locations.</p>
                    
                    <p><strong>Level 2:</strong> Here, our support team are strategically positioned in-house to support your day-to-day operations and address challenges that may arise in either network or other IT related needs as required.</p>
                    
                    <p>Whether its a temporary contract or a permanent placement, with a range of experts to choose from, AthenaNg can help to augment your IT staff as needed.</p>
                ''',
                'features': [
                    {
                        'title': 'Level 1 & 2 Support',
                        'description': 'Comprehensive support levels for diverse IT needs.',
                        'icon': 'bi-headset'
                    },
                    {
                        'title': 'Flexible Staffing',
                        'description': 'Temporary, contract, or permanent staffing solutions.',
                        'icon': 'bi-person-badge'
                    },
                    {
                        'title': 'Expert Matching',
                        'description': 'Match your needs with specialized IT professionals.',
                        'icon': 'bi-people'
                    },
                    {
                        'title': 'Cost-Effective',
                        'description': 'Reduce hiring costs with flexible staffing solutions.',
                        'icon': 'bi-cash-stack'
                    }
                ],
                'benefits': [
                    'Access to specialized IT expertise',
                    'Flexible staffing arrangements',
                    'Reduced hiring and training costs',
                    'Quick response to staffing needs',
                    'Scalable support options',
                    'Proven Fortune 100 experience'
                ],
                'process': [
                    {
                        'step': 1,
                        'title': 'Needs Assessment',
                        'description': 'Evaluate staffing and support requirements'
                    },
                    {
                        'step': 2,
                        'title': 'Expert Matching',
                        'description': 'Match requirements with qualified professionals'
                    },
                    {
                        'step': 3,
                        'title': 'Onboarding',
                        'description': 'Smooth integration of staff into your team'
                    },
                    {
                        'step': 4,
                        'title': 'Ongoing Management',
                        'description': 'Continuous support and performance management'
                    }
                ],
                'technologies': [
                    'Network Support Tools',
                    'Help Desk Software',
                    'Remote Support Solutions',
                    'Monitoring Systems',
                    'ITSM Platforms',
                    'Collaboration Tools'
                ],
                'stats': [
                    {
                        'value': 'Flexible',
                        'label': 'Staffing Options'
                    },
                    {
                        'value': 'Expert',
                        'label': 'Team Matching'
                    },
                    {
                        'value': 'Cost-Effective',
                        'label': 'Solutions'
                    },
                    {
                        'value': '24/7',
                        'label': 'Support Available'
                    }
                ]
            }
        },
        'sdn': {
            'template': 'core/service-details.html',
            'title': 'Software Defined Network Services',
            'description': 'SDN solutions for programmable network management',
            'icon': 'bi-code-slash',
            'data': {
                'hero_title': 'Software Defined Network Services',
                'hero_description': 'We combine both experience and modern sophisticated software-based controllers as an approach to enhance communication with underlying hardware infrastructure and direct traffic on your business/organization network.',
                'overview': 'Software Defined Networking (SDN) enables the programming of network behavior in a centrally controlled manner through software applications using open APIs.',
                'full_description': '''
                    <p>This helps you manage the entire network consistently and holistically, regardless of the underlying network technology.</p>
                    
                    <p>By opening up traditionally closed network platforms and implementing a common SDN control layer, your organization can manage the entire network and its devices consistently, regardless of the complexity of the underlying network technology.</p>
                    
                    <p>AthenaNg simply offers a consulting-led approach that helps you and your organization create the cloud-enabled and resilient network that you need.</p>
                ''',
                'features': [
                    {
                        'title': 'Centralized Control',
                        'description': 'Unified network management through software controllers.',
                        'icon': 'bi-layers'
                    },
                    {
                        'title': 'Network Virtualization',
                        'description': 'Abstract network hardware for flexible configuration.',
                        'icon': 'bi-cpu'
                    },
                    {
                        'title': 'API Programming',
                        'description': 'Programmable network behavior through open APIs.',
                        'icon': 'bi-code-square'
                    },
                    {
                        'title': 'Cloud Integration',
                        'description': 'Seamless integration with cloud environments.',
                        'icon': 'bi-cloud'
                    }
                ],
                'benefits': [
                    'Centralized network management',
                    'Improved network agility and flexibility',
                    'Reduced operational costs',
                    'Enhanced security through segmentation',
                    'Better resource utilization',
                    'Faster service deployment'
                ],
                'process': [
                    {
                        'step': 1,
                        'title': 'SDN Assessment',
                        'description': 'Evaluate current infrastructure for SDN readiness'
                    },
                    {
                        'step': 2,
                        'title': 'Architecture Design',
                        'description': 'Design SDN architecture and migration plan'
                    },
                    {
                        'step': 3,
                        'title': 'Implementation',
                        'description': 'Deploy SDN controllers and configure network'
                    },
                    {
                        'step': 4,
                        'title': 'Optimization',
                        'description': 'Fine-tune and optimize SDN performance'
                    }
                ],
                'technologies': [
                    'Cisco ACI',
                    'VMware NSX',
                    'OpenFlow',
                    'OpenStack',
                    'SD-WAN Solutions',
                    'Network Automation'
                ],
                'stats': [
                    {
                        'value': 'Centralized',
                        'label': 'Network Control'
                    },
                    {
                        'value': 'API-Driven',
                        'label': 'Management'
                    },
                    {
                        'value': 'Cloud-Enabled',
                        'label': 'Architecture'
                    },
                    {
                        'value': 'Virtualized',
                        'label': 'Network Solutions'
                    }
                ]
            }
        },
        'digital-archiving': {
            'template': 'core/service-details.html',
            'title': 'Digital & Archiving',
            'description': 'Comprehensive digital archiving and document management solutions',
            'icon': 'bi-archive',
            'data': {
                'hero_title': 'Digital & Archiving',
                'hero_description': 'Technology has come to changed the way organizations store vital information or documents from the traditional bulky files in cabinets that consume space to digital archiving them.',
                'overview': 'With the advent of cloud storage and virtual servers that can accommodate any volume of data and access on the go, document and photograph archival in digital mode is the best choice.',
                'full_description': '''
                    <p>Hard copies occupy considerable space and are liable to be lost, damaged, or deliberately manipulated. Business information that are critical and relying on hard copy versions of data can prove fatal in the long run.</p>
                    
                    <p>AthenaNg Consulting offers a complete spectrum of digital archiving services to companies and organizations worldwide. Organizations across a wide range of operational domains like healthcare, education, financial, legal, public service, etc. trust our bespoke document archiving services.</p>
                    
                    <h5>Time to go paperless with us</h5>
                    <p>As digital communication through email or (enterprise) social networks is increasing, financial solutions are more and more digitized, medical patient files are digitized and accessible to all the professionals and the patients.</p>
                    
                    <p>This results in an increasing amount of digital information and documents that need to be managed properly. This is where we come in with our years of accumulated experience in archiving and cloud storage capabilities. We have available dedicated servers with large storage capacities to handle all your document storage and ensure they are safely kept and easily retrievable.</p>
                    
                    <p>We have also established a long standing partnership with our cloud service partners like Amazon, Microsoft and Google to ensure we offer seamlessly effective integrated digital and archiving solutions.</p>
                ''',
                'features': [
                    {
                        'title': 'Document Digitization',
                        'description': 'Convert physical documents to secure digital formats.',
                        'icon': 'bi-scanner'
                    },
                    {
                        'title': 'Cloud Storage',
                        'description': 'Secure cloud storage with major providers.',
                        'icon': 'bi-cloud-upload'
                    },
                    {
                        'title': 'Metadata Tagging',
                        'description': 'Advanced metadata organization for easy retrieval.',
                        'icon': 'bi-tags'
                    },
                    {
                        'title': 'Compliance Management',
                        'description': 'Ensure compliance with industry regulations.',
                        'icon': 'bi-shield-check'
                    }
                ],
                'benefits': [
                    'Secure document storage and retrieval',
                    'Significant space savings',
                    'Improved document accessibility',
                    'Enhanced data security',
                    'Regulatory compliance',
                    'Disaster recovery protection'
                ],
                'process': [
                    {
                        'step': 1,
                        'title': 'Document Assessment',
                        'description': 'Evaluate document types and archiving needs'
                    },
                    {
                        'step': 2,
                        'title': 'Digitization',
                        'description': 'Convert physical documents to digital formats'
                    },
                    {
                        'step': 3,
                        'title': 'Organization',
                        'description': 'Apply metadata and categorization'
                    },
                    {
                        'step': 4,
                        'title': 'Storage & Access',
                        'description': 'Secure storage with controlled access'
                    }
                ],
                'technologies': [
                    'Document Management Systems',
                    'Cloud Storage (AWS, Azure, Google)',
                    'OCR Technology',
                    'Metadata Management',
                    'Compliance Software',
                    'Backup Solutions'
                ],
                'stats': [
                    {
                        'value': 'Since 2010',
                        'label': 'Archiving Experience'
                    },
                    {
                        'value': 'Cloud',
                        'label': 'Storage Partners'
                    },
                    {
                        'value': 'Secure',
                        'label': 'Document Management'
                    },
                    {
                        'value': 'Global',
                        'label': 'Client Base'
                    }
                ]
            }
        },
        'network-audits': {
            'template': 'core/service-details.html',
            'title': 'Network Audits & Compliance',
            'description': 'Comprehensive network security audits and compliance assessments',
            'icon': 'bi-clipboard-check',
            'data': {
                'hero_title': 'Network Audits & Compliance',
                'hero_description': 'When was the last time that you and your team performed an audit? A lot can change overtime such as new and existing application demands on the network.',
                'overview': 'Network audit and compliance is a fairly complex task but many business organizations who truly understand the impact, realize that periodic examinations can actually help ensure that security strategies are in sync with overall business activities and goals.',
                'full_description': '''
                    <p>At AthenaNg Consulting, we follow a well defined best practices model to perform network audits. Our team of expert with decades of experience accomplish their job though personal interviews, vulnerability scans, examination of Operating Systems and security-application settings and network analyses as well as studying historical data such as event logs.</p>
                    
                    <p>Auditors also focus on the your organization's security policies to determine what they cover, how they are used and whether they are effective at meeting ongoing and future threats.</p>
                    
                    <p>Trust AthenaNg to audit your network infrastructure, find and eliminate gaps, and keep fully compliant with prevailing security standards.</p>
                ''',
                'features': [
                    {
                        'title': 'Security Audits',
                        'description': 'Comprehensive security posture assessment.',
                        'icon': 'bi-shield-check'
                    },
                    {
                        'title': 'Vulnerability Scanning',
                        'description': 'Identify security vulnerabilities and risks.',
                        'icon': 'bi-search'
                    },
                    {
                        'title': 'Compliance Assessment',
                        'description': 'Ensure adherence to industry standards.',
                        'icon': 'bi-file-check'
                    },
                    {
                        'title': 'Policy Review',
                        'description': 'Evaluate and improve security policies.',
                        'icon': 'bi-journal-text'
                    }
                ],
                'benefits': [
                    'Improved network security posture',
                    'Regulatory compliance assurance',
                    'Identification of security gaps',
                    'Risk mitigation strategies',
                    'Enhanced data protection',
                    'Peace of mind for stakeholders'
                ],
                'process': [
                    {
                        'step': 1,
                        'title': 'Discovery',
                        'description': 'interviews and documentation review'
                    },
                    {
                        'step': 2,
                        'title': 'Assessment',
                        'description': 'Vulnerability scanning and security testing'
                    },
                    {
                        'step': 3,
                        'title': 'Analysis',
                        'description': 'Detailed analysis of findings and risks'
                    },
                    {
                        'step': 4,
                        'title': 'Reporting',
                        'description': 'Comprehensive report with recommendations'
                    }
                ],
                'technologies': [
                    'Vulnerability Scanners',
                    'Network Analyzers',
                    'SIEM Tools',
                    'Compliance Frameworks',
                    'Penetration Testing Tools',
                    'Security Assessment Platforms'
                ],
                'stats': [
                    {
                        'value': 'Comprehensive',
                        'label': 'Security Audits'
                    },
                    {
                        'value': 'Regulatory',
                        'label': 'Compliance Focus'
                    },
                    {
                        'value': 'Risk',
                        'label': 'Mitigation Strategies'
                    },
                    {
                        'value': 'Expert',
                        'label': 'Assessment Teams'
                    }
                ]
            }
        },
        'core-network': {
            'template': 'core/service-details.html',
            'title': 'Core Network & IP Planning',
            'description': 'Core network infrastructure design and IP management solutions',
            'icon': 'bi-hdd-rack',
            'data': {
                'hero_title': 'Core Network & IP Planning',
                'hero_description': 'AthenaNg has for over many decades been noted for effectively executing Core Network and IP Planning services to many organizations world-wide.',
                'overview': 'We have implemented over 2000 core network and IP Planning services to over 580 clients globally with the majority in Asia and Europe. Our clients outsource this major aspect of their operations to us because of competency and years of experience in this area.',
                'full_description': '''
                    <p>Core Network services are the solid foundation for building secure, compliant networks which is why we channel every efforts into its execution and pay critical attention to its management.</p>
                    
                    <p>Basically, all resources on your network depends to a large extent on the core network services like DDI (DNS, DHCP and IP address management) and NTP which are often invisible, but without them your network and your business grinds to a halt.</p>
                    
                    <p>Enterprise solutions for Core Network Services must be architected for high availability and include the capability to monitor, optimize and report on their operations and performance, and to proactively detect issues and anomalies before end users are impacted.</p>
                    
                    <p>The combination of on-premises, virtual and cloud infrastructure as well as digital transformations like SD-WAN, multi-cloud and IOT have all put more importance on having an effective strategy and flawless performance on your Core Network Services.</p>
                    
                    <p>AthenaNg has a full range of professional services to guide your successful journey with Core Network and IP Planning Services in addition to complete implementations and training for your team.</p>
                ''',
                'features': [
                    {
                        'title': 'DDI Services',
                        'description': 'DNS, DHCP, and IP address management solutions.',
                        'icon': 'bi-hdd-network'
                    },
                    {
                        'title': 'High Availability',
                        'description': 'Fault-tolerant core network architectures.',
                        'icon': 'bi-lightning-charge'
                    },
                    {
                        'title': 'IP Planning',
                        'description': 'Strategic IP address planning and management.',
                        'icon': 'bi-diagram-3'
                    },
                    {
                        'title': 'Multi-Cloud Integration',
                        'description': 'Core network services for hybrid environments.',
                        'icon': 'bi-clouds'
                    }
                ],
                'benefits': [
                    'Highly available network infrastructure',
                    'Efficient IP address management',
                    'Reduced network downtime',
                    'Scalable core network design',
                    'Enhanced network performance',
                    'Future-proof architecture'
                ],
                'process': [
                    {
                        'step': 1,
                        'title': 'Requirements Analysis',
                        'description': 'Assess core network needs and constraints'
                    },
                    {
                        'step': 2,
                        'title': 'IP Planning',
                        'description': 'Design IP addressing scheme and architecture'
                    },
                    {
                        'step': 3,
                        'title': 'Implementation',
                        'description': 'Deploy core network infrastructure'
                    },
                    {
                        'step': 4,
                        'title': 'Optimization',
                        'description': 'Fine-tune and monitor core network performance'
                    }
                ],
                'technologies': [
                    'DNS Servers',
                    'DHCP Solutions',
                    'IPAM Tools',
                    'Load Balancers',
                    'High Availability Clusters',
                    'Network Monitoring'
                ],
                'stats': [
                    {
                        'value': '2000+',
                        'label': 'Core Networks'
                    },
                    {
                        'value': '580+',
                        'label': 'Global Clients'
                    },
                    {
                        'value': 'High',
                        'label': 'Availability'
                    },
                    {
                        'value': 'Enterprise',
                        'label': 'Grade Solutions'
                    }
                ]
            }
        },
        'information-security': {
            'template': 'core/service-details.html',
            'title': 'Information Security',
            'description': 'Comprehensive cybersecurity and information protection solutions',
            'icon': 'bi-shield-lock',
            'data': {
                'hero_title': 'Information Security',
                'hero_description': "At AthenaNg, we are committed to helping you achieve your security goals by identifying whether it's training that your team needs or adhering to standards, product testing or general consultation.",
                'overview': "Globally, the cyber threat landscape is constantly evolving and increasingly becoming complex but most organizations don't have the required security tools and capacity in-house to keep security measures up-to-date and ensure optimum protection of their data.",
                'full_description': '''
                    <p>Whatever the need may be, we empower you to keep your business safe through a diverse portfolio of information security solutions.</p>
                    
                    <p>For this reason, many organizations have become vulnerable, making it easier for hackers to initiate attacks. These attacks, when successfully executed can lead to the loss of millions — not to mention the harm to brand's reputation.</p>
                    
                    <p>It's imperative therefore that, businesses adopt a layered approach to tackle attacks on network through advanced threat protection solutions from AthenaNg. We have a multi-faceted prevention strategy combining proactive protection, which eliminates threats before they reach users, and state-of-the-art CPU-level exploit detection tools, which detects highly camouflaged threats.</p>
                    
                    <p>Our team of experts evaluates high-impact solutions with persistent research and current regulatory standards to ensure we offer 101% security solutions to secure the data of our clients.</p>
                    
                    <p>At AthenaNg, we guarantee you complete protection of your applications, products, and infrastructure against cyber threats, possible data leaks, thefts, or disasters. By reducing possible damages and providing full control over privacy and compliance, all your shared data, business intelligence, and other assets can be managed securely without risks.</p>
                ''',
                'features': [
                    {
                        'title': 'Threat Protection',
                        'description': 'Advanced protection against evolving cyber threats.',
                        'icon': 'bi-shield-slash'
                    },
                    {
                        'title': 'Security Assessment',
                        'description': 'Comprehensive security posture evaluation.',
                        'icon': 'bi-search'
                    },
                    {
                        'title': 'Compliance Management',
                        'description': 'Ensure adherence to security standards.',
                        'icon': 'bi-file-check'
                    },
                    {
                        'title': 'Incident Response',
                        'description': 'Rapid response to security incidents.',
                        'icon': 'bi-exclamation-triangle'
                    }
                ],
                'benefits': [
                    'Comprehensive threat protection',
                    'Regulatory compliance assurance',
                    'Reduced security risks',
                    'Enhanced data privacy',
                    'Proactive security monitoring',
                    'Peace of mind for stakeholders'
                ],
                'process': [
                    {
                        'step': 1,
                        'title': 'Security Assessment',
                        'description': 'Evaluate current security posture'
                    },
                    {
                        'step': 2,
                        'title': 'Strategy Development',
                        'description': 'Create comprehensive security strategy'
                    },
                    {
                        'step': 3,
                        'title': 'Implementation',
                        'description': 'Deploy security solutions and controls'
                    },
                    {
                        'step': 4,
                        'title': 'Monitoring & Response',
                        'description': 'Continuous monitoring and incident response'
                    }
                ],
                'technologies': [
                    'Firewall Solutions',
                    'Intrusion Prevention',
                    'SIEM Platforms',
                    'Endpoint Protection',
                    'Encryption Tools',
                    'Compliance Software'
                ],
                'stats': [
                    {
                        'value': 'Multi-Layered',
                        'label': 'Security Approach'
                    },
                    {
                        'value': '101%',
                        'label': 'Security Solutions'
                    },
                    {
                        'value': 'Proactive',
                        'label': 'Threat Protection'
                    },
                    {
                        'value': 'Compliance',
                        'label': 'Focused'
                    }
                ]
            }
        },
        'cloud-computing': {
            'template': 'core/service-details.html',
            'title': 'Cloud Computing',
            'description': 'Cloud migration, management, and optimization services',
            'icon': 'bi-cloud-arrow-up',
            'data': {
                'hero_title': 'Cloud Computing',
                'hero_description': "Whether you're an IT team looking to outsource the management of a cloud application or a business that needs help migrating to the cloud, we can help.",
                'overview': 'We are a one-stop cloud service provider for many businesses with diverse options, so whether your applications are running in an on-premise data center, a third-party hosted cloud or a combination of the two, we can help you become more agile and responsive to the changing market landscape.',
                'full_description': '''
                    <p>At AthenaNg, we assist customers with our on-demand delivery of computing services, tools and applications such as servers, storage, databases, networking, software, applications among others.</p>
                    
                    <p>We take a strategic approach to implementing cloud consulting services so as to enable organizations to reduce IT resource requirements, improve productivity and help in right decision-making to maximizing Return on Investment (ROI).</p>
                    
                    <p>Our cloud computing solutions ensure a seamless transition to the cloud professionally with ease. We can scale and migrate your chosen application workloads securely with speed.</p>
                    
                    <p>Our approach includes: Assessment, Planning, Deployment and Optimization.</p>
                ''',
                'features': [
                    {
                        'title': 'Cloud Migration',
                        'description': 'Seamless migration to cloud platforms.',
                        'icon': 'bi-cloud-arrow-up'
                    },
                    {
                        'title': 'Cloud Management',
                        'description': 'Comprehensive cloud infrastructure management.',
                        'icon': 'bi-gear'
                    },
                    {
                        'title': 'Cost Optimization',
                        'description': 'Optimize cloud spending and resource utilization.',
                        'icon': 'bi-graph-up'
                    },
                    {
                        'title': 'Multi-Cloud Strategy',
                        'description': 'Strategies for hybrid and multi-cloud environments.',
                        'icon': 'bi-clouds'
                    }
                ],
                'benefits': [
                    'Reduced IT infrastructure costs',
                    'Improved scalability and flexibility',
                    'Enhanced business agility',
                    'Better resource utilization',
                    'Increased ROI on cloud investments',
                    'Expert cloud strategy guidance'
                ],
                'process': [
                    {
                        'step': 1,
                        'title': 'Cloud Assessment',
                        'description': 'Evaluate cloud readiness and requirements'
                    },
                    {
                        'step': 2,
                        'title': 'Migration Planning',
                        'description': 'Develop comprehensive migration strategy'
                    },
                    {
                        'step': 3,
                        'title': 'Deployment',
                        'description': 'Execute cloud migration and deployment'
                    },
                    {
                        'step': 4,
                        'title': 'Optimization',
                        'description': 'Optimize cloud performance and costs'
                    }
                ],
                'technologies': [
                    'AWS (Amazon Web Services)',
                    'Microsoft Azure',
                    'Google Cloud Platform',
                    'Cloud Management Tools',
                    'Container Orchestration',
                    'Serverless Computing'
                ],
                'stats': [
                    {
                        'value': 'One-Stop',
                        'label': 'Cloud Provider'
                    },
                    {
                        'value': 'ROI',
                        'label': 'Optimization Focus'
                    },
                    {
                        'value': 'Seamless',
                        'label': 'Migration Process'
                    },
                    {
                        'value': 'Multi-Cloud',
                        'label': 'Expertise'
                    }
                ]
            }
        },
    }
    
    # Get the service data or return 404
    if service_slug not in services_data:
        from django.http import Http404
        raise Http404("Service not found")
    
    service_info = services_data[service_slug]
    context = {
        'title': service_info['title'],
        'description': service_info['description'],
        'service': service_info['data'],
        'service_slug': service_slug,
        'icon': service_info['icon']
    }
    
    return render(request, service_info['template'], context)


def careers(request):
    template_name = "core/careers.html"
    
    # Sample job openings data - you can make this dynamic by connecting to a database
    job_openings = [
        {
            'id': 1,
            'title': 'Linux / Private Cloud Engineer',
            'department': 'Cloud Computing',
            'location': 'Miami, FL (Hybrid)',
            'type': 'Full-time',
            'experience': '3-5 years',
            'posted_date': '2024-01-15',
            'description': 'Design, implement, and maintain private cloud infrastructure using Linux-based solutions.',
            'requirements': [
                'Bachelor\'s degree in Computer Science or related field',
                '3+ years experience with Linux administration',
                'Experience with OpenStack, VMware, or similar cloud platforms',
                'Strong knowledge of networking and security protocols',
                'Experience with automation tools (Ansible, Terraform)'
            ]
        },
        {
            'id': 2,
            'title': 'Field Technician',
            'department': 'Network Deployment',
            'location': 'Various Locations (Travel Required)',
            'type': 'Full-time',
            'experience': '2-4 years',
            'posted_date': '2024-01-10',
            'description': 'Install, maintain, and troubleshoot network equipment at client sites across multiple locations.',
            'requirements': [
                'Associate degree or technical certification in Networking',
                '2+ years field experience in telecom or networking',
                'Familiarity with fiber optics, cabling, and network hardware',
                'Valid driver\'s license and ability to travel',
                'Strong troubleshooting skills'
            ]
        },
        {
            'id': 3,
            'title': 'Network Security Analyst',
            'department': 'Information Security',
            'location': 'Remote',
            'type': 'Full-time',
            'experience': '4-6 years',
            'posted_date': '2024-01-05',
            'description': 'Monitor, analyze, and respond to security threats across client networks.',
            'requirements': [
                'Bachelor\'s degree in Cybersecurity or related field',
                '4+ years in network security operations',
                'Certifications: Security+, CISSP, or similar',
                'Experience with SIEM tools and threat detection',
                'Knowledge of compliance standards (NIST, ISO 27001)'
            ]
        },
        {
            'id': 4,
            'title': 'Systems Integration Specialist',
            'department': 'Systems Integration',
            'location': 'Miami, FL',
            'type': 'Full-time',
            'experience': '3-5 years',
            'posted_date': '2024-01-03',
            'description': 'Integrate diverse IT systems and applications for enterprise clients.',
            'requirements': [
                'Bachelor\'s degree in IT or related field',
                '3+ years experience in systems integration',
                'Knowledge of API development and middleware',
                'Experience with ERP and CRM systems',
                'Strong problem-solving skills'
            ]
        },
        {
            'id': 5,
            'title': 'Digital Archiving Consultant',
            'department': 'Digital Solutions',
            'location': 'Remote',
            'type': 'Contract',
            'experience': '2-3 years',
            'posted_date': '2023-12-28',
            'description': 'Implement and customize digital archiving solutions for clients.',
            'requirements': [
                'Experience with document management systems',
                'Knowledge of Square 9 or similar platforms',
                'Understanding of compliance requirements',
                'Project management skills',
                'Client consultation experience'
            ]
        },
        {
            'id': 6,
            'title': 'Junior Network Engineer',
            'department': 'Network Operations',
            'location': 'Miami, FL',
            'type': 'Full-time',
            'experience': '1-2 years',
            'posted_date': '2023-12-20',
            'description': 'Assist in network design, deployment, and maintenance under senior guidance.',
            'requirements': [
                'Bachelor\'s degree in Networking or related field',
                'CCNA or similar certification preferred',
                'Basic understanding of routing and switching',
                'Willingness to learn and grow',
                'Strong communication skills'
            ]
        }
    ]
    
    context = {
        'title': 'Careers',
        'description': 'Join our team of technology experts at AthenaNG Consulting',
        'job_openings': job_openings
    }
    return render(request, template_name, context)


def privacy_policy(request):
    template_name = "core/privacy-policy.html"
    context = {}
    return render(request, template_name, context)


def terms_of_service(request):
    template_name = "core/terms-of-service.html"
    context = {}
    return render(request, template_name, context)
