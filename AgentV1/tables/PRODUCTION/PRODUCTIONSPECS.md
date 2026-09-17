# DB2ADMIN.PRODUCTIONSPECS

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `business_data`
- **Columns**: 35
- **Primary key**: `COMPANYCODE`, `WORKCENTERCODE`, `OPERATIONCODE`, `WRKCTRANDOPERATTRCODE`, `RESOURCEGROUPCODE`, `RESOURCECODE`, `ITEMTYPEAFICODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`, `USERGROUPTYPECODE`, `USERGROUPCODE`, `INITIALDATE`, `FINALDATE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 95228

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `INITIALDATE` | DATE | NOT NULL | PK | primary_key |  |
| 2 | `FINALDATE` | DATE | NOT NULL | PK | primary_key |  |
| 3 | `TEMPLATECODE` | CHAR(8) |  | FK | foreign_key |  |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `WORKCENTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 8 | `OPERATIONCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 9 | `WRKCTRANDOPERATTRCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 10 | `RESOURCEGROUPCODE` | CHAR(5) | NOT NULL | PK | primary_key |  |
| 11 | `RESOURCECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 12 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 13 | `ITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 14 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 15 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 16 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 17 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 18 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 19 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 20 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 21 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 22 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 23 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 24 | `USERGROUPTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 25 | `USERGROUPTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 26 | `USERGRPUSERGENGRPTYPECMYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 27 | `USERGROUPCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 28 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 29 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 30 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 31 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 32 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 33 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 34 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRODUCTIONSPECS.COMPANYCODE = COMPANY.CODE` |
| `PRODUCTIONSPECSTEMPLATE_TEMPLATE` | `COMPANYCODE`, `TEMPLATECODE` | [`PRODUCTIONSPECSTEMPLATE`](../PRODUCTION/PRODUCTIONSPECSTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONSPECS.COMPANYCODE = PRODUCTIONSPECSTEMPLATE.COMPANYCODE AND PRODUCTIONSPECS.TEMPLATECODE = PRODUCTIONSPECSTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRODUCTIONSPECSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.INITIALDATE,
       t.FINALDATE,
       t.TEMPLATECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.WORKCENTERCODE,
       t.OPERATIONCODE,
       t.WRKCTRANDOPERATTRCODE,
       t.RESOURCEGROUPCODE,
       t.RESOURCECODE
FROM   DB2ADMIN.PRODUCTIONSPECS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
