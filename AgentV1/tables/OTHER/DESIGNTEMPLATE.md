# DB2ADMIN.DESIGNTEMPLATE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 26
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 28740

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `USRGENGRPTYPMODE` | CHAR(1) |  |  |  |  |
| 6 | `KEYNUMBERDES` | DECIMAL(2,0) |  |  |  |  |
| 7 | `SUBSTRFROMUSRGENGRPTYPDES` | DECIMAL(2,0) |  |  |  |  |
| 8 | `SUBSTRNOCHARSUSRGENGRPTYPDES` | DECIMAL(2,0) |  |  |  |  |
| 9 | `USRGENGRPTYPDESCODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `DELETEUSRGENGRPTYPDES` | SMALLINT | NOT NULL |  |  |  |
| 11 | `SUBSTRFROMUSRGENGRPTYPVAR` | DECIMAL(2,0) |  |  |  |  |
| 12 | `SUBSTRNOCHARSUSRGENGRPTYPVAR` | DECIMAL(2,0) |  |  |  |  |
| 13 | `USRGENGRPTYPVARCODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `DELETEUSRGENGRPTYPVAR` | SMALLINT | NOT NULL |  |  |  |
| 15 | `CHECKPOLICYCODE` | CHAR(20) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `USRGENGRPTYPDESCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 22 | `USRGENGRPTYPVARCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 23 | `SCREENSAREPRODUCTNATURE` | SMALLINT | NOT NULL |  |  |  |
| 24 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 25 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `DESIGNTEMPLATE.COMPANYCODE = COMPANY.CODE` |
| `USERGENERICGROUPTYPE_USRGENGRPTYPDES` | `USRGENGRPTYPDESCOMPANYCODE`, `USRGENGRPTYPDESCODE` | [`USERGENERICGROUPTYPE`](../CORE_MASTER/USERGENERICGROUPTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DESIGNTEMPLATE.USRGENGRPTYPDESCOMPANYCODE = USERGENERICGROUPTYPE.COMPANYCODE AND DESIGNTEMPLATE.USRGENGRPTYPDESCODE = USERGENERICGROUPTYPE.CODE` |
| `USERGENERICGROUPTYPE_USRGENGRPTYPVAR` | `USRGENGRPTYPVARCOMPANYCODE`, `USRGENGRPTYPVARCODE` | [`USERGENERICGROUPTYPE`](../CORE_MASTER/USERGENERICGROUPTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DESIGNTEMPLATE.USRGENGRPTYPVARCOMPANYCODE = USERGENERICGROUPTYPE.COMPANYCODE AND DESIGNTEMPLATE.USRGENGRPTYPVARCODE = USERGENERICGROUPTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DESIGNTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.USRGENGRPTYPMODE,
       t.KEYNUMBERDES,
       t.SUBSTRFROMUSRGENGRPTYPDES,
       t.SUBSTRNOCHARSUSRGENGRPTYPDES,
       t.USRGENGRPTYPDESCODE,
       t.DELETEUSRGENGRPTYPDES,
       t.SUBSTRFROMUSRGENGRPTYPVAR
FROM   DB2ADMIN.DESIGNTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
