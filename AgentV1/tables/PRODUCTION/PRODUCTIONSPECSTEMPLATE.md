# DB2ADMIN.PRODUCTIONSPECSTEMPLATE

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `business_data`
- **Columns**: 34
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 95312

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(8) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `WORKCENTERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `OPERATIONREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 7 | `WRKCTRANDOPERATTRREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `RESOURCEGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 9 | `RESOURCEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 10 | `ITEMTYPEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 11 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `ITEMREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 14 | `SUBCODE01CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 15 | `SUBCODE02CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 16 | `SUBCODE03CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 17 | `SUBCODE04CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 18 | `SUBCODE05CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 19 | `SUBCODE06CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 20 | `SUBCODE07CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 21 | `SUBCODE08CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 22 | `SUBCODE09CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 23 | `SUBCODE10CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 24 | `INPUTUSERGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 25 | `INPUTUSERGROUPCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 26 | `INPUTUSERGROUPCODE` | CHAR(3) |  | FK | foreign_key |  |
| 27 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 28 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 29 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 30 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 31 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 32 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 33 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRODUCTIONSPECSTEMPLATE.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONSPECSTEMPLATE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND PRODUCTIONSPECSTEMPLATE.ITEMTYPECODE = ITEMTYPE.CODE` |
| `USERGENERICGROUPTYPE_INPUTUSERGROUP` | `INPUTUSERGROUPCOMPANYCODE`, `INPUTUSERGROUPCODE` | [`USERGENERICGROUPTYPE`](../CORE_MASTER/USERGENERICGROUPTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONSPECSTEMPLATE.INPUTUSERGROUPCOMPANYCODE = USERGENERICGROUPTYPE.COMPANYCODE AND PRODUCTIONSPECSTEMPLATE.INPUTUSERGROUPCODE = USERGENERICGROUPTYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PRODUCTIONSPECSTEMPLATE_TEMPLATE` | [`PRODUCTIONSPECS`](../PRODUCTION/PRODUCTIONSPECS.md) | `COMPANYCODE`, `TEMPLATECODE` | `PRODUCTIONSPECS.COMPANYCODE = PRODUCTIONSPECSTEMPLATE.COMPANYCODE AND PRODUCTIONSPECS.TEMPLATECODE = PRODUCTIONSPECSTEMPLATE.CODE` |

## Indexes

- `PRODUCTIONSPECSTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.WORKCENTERREQUIRED,
       t.OPERATIONREQUIRED,
       t.WRKCTRANDOPERATTRREQUIRED,
       t.RESOURCEGROUPREQUIRED,
       t.RESOURCEREQUIRED,
       t.ITEMTYPEREQUIRED,
       t.ITEMTYPECOMPANYCODE
FROM   DB2ADMIN.PRODUCTIONSPECSTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
