#!/usr/bin/env python

import sys,os

# !in this way docs source module, not the installed one
sys.path.insert(0, os.path.abspath('../'))

import argparse
import asterism
import pkgutil

package = asterism

print package.__path__

def make_module_uml(modname):

    cmd="pyreverse   %s -AS -mn -k -o png -p rel_%s "%(modname,modname)
    print cmd
    os.system(cmd)
    cmd="mv classes_rel_%s.png  source/modules_doc/"%modname
    os.system(cmd)


    cmd="pyreverse   %s   -o png -p %s "%(modname,modname)
    print cmd
    os.system(cmd)
    cmd="mv classes_%s.png  source/modules_doc/"%modname
    os.system(cmd)


def find_max_subpackage_levels(package_list):
    max_l=0
    for p in package_list:
        l=len(p.split('.'))
        max_l=max(l,max_l)

    return max_l


def build_level_subpackage_list(package_list,level):
    pack_list=[]
    for p_name in package_list:
        sp_names=p_name.split('.')
        if len(sp_names)>level:
            name='.'.join(str(e) for e in sp_names[0:level+1])
            if name not in pack_list:
                pack_list.append(name)

    return pack_list

def write_packages_toc_file(api_dir,sub_packages_list,root_package,mod_list):

    hdr="""
package: %s
=========================

Subpackages
-----------

.. toctree::
   :maxdepth: 1

"""%root_package


    f=open('%s/%s.rst'%(api_dir,root_package),'w')
    #print '%s/%s.rst'%(api_dir,root_package)
    print>>f,hdr
    print "developing root",root_package
    for package_name in sub_packages_list:
        if root_package  in package_name and root_package!=package_name:
            #mame=package_name.split('.')[-1]
            print>>f,"   %s "%(package_name)
            print" -root", root_package,package_name


    text="""
Modules
---------------
.. toctree::
   :maxdepth: 1

"""
    print>>f,text
    for mod_name in mod_list:
        name='.'.join(str(e) for e in mod_name.split('.')[0:-1])
        #print "->",name,root_package
        if root_package  ==name:
            #mame=package_name.split('.')[-1]
            print>>f,"  %s "%(mod_name)


    f.close()



def make_apidoc_pkg(api_dir,pakage_list,mod_list):

    max_level=find_max_subpackage_levels(pakage_list)
    print("max level",max_level)
    level_list=[]
    for level in xrange(max_level):

        sub_level_list=build_level_subpackage_list(pakage_list,level)
        print "level ",level, sub_level_list
        level_list.append(sub_level_list)


    for level in xrange(max_level):
        for root_package in level_list[level]:

            #for sub_pacakge in level_list[level+1]:
            print "root is ",root_package
            if level<max_level-1:
                write_packages_toc_file(api_dir,level_list[level+1],root_package,mod_list)
            else:
                write_packages_toc_file(api_dir,level_list[level],root_package,mod_list)
    #write_packages_toc_file(wd,sub_packages_list,)

def write_mod_file(api_dir,mod_name):
    text="""


Module: %s
---------------

.. automodule:: %s
    :members:
    :undoc-members:
    :show-inheritance:
    """%(mod_name.split('.')[-1],mod_name)

    f=open('%s/%s.rst'%(api_dir,mod_name),'w')
    print>>f,text
    f.close()


def make_apidoc_mod(api_dir,mod_list):


    for mod_name in mod_list:
        write_mod_file(api_dir,mod_name)


def run(api_dir='./'):
    mod_list=[]
    pakage_list=[]
    for importer, modname, ispkg in pkgutil.walk_packages(path=asterism.__path__,
                                                      prefix=package.__name__+'.',
                                                      onerror=lambda x: None):
        print "Found submodule %s " % (modname)
        if ispkg==True:
            pakage_list.append(modname)
        else:
            mod_list.append(modname)
           # print "subpackage",modname
    #print mod_list

    make_apidoc_pkg(api_dir,pakage_list,mod_list)
    make_apidoc_mod(api_dir,mod_list)

def main (argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('api_dir', type=str, default='./' )
    args = parser.parse_args()
    run(api_dir=args.api_dir)

if __name__=="__main__":
	main(sys.argv)