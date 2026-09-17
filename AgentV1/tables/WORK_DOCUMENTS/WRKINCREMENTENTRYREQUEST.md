# DB2ADMIN.WRKINCREMENTENTRYREQUEST

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 42
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `INCREMENTNO`, `EMPLOYEECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 171128

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `INCREMENTNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `CATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 5 | `CATEGORYCODE` | CHAR(6) |  |  |  |  |
| 6 | `SUBCTGSUBCATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 7 | `SUBCATEGORYSUBCATEGORYCODE` | CHAR(6) |  |  |  |  |
| 8 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 9 | `FACTORYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 10 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 11 | `DEPARTMENTDEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 12 | `NEWDEPARTMENTDEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 13 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 14 | `OLDGRADE` | CHAR(6) |  |  |  |  |
| 15 | `NEWGRADEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 16 | `NEWGRADECODE` | CHAR(6) |  |  |  |  |
| 17 | `OLDBASIC` | DECIMAL(11,2) |  |  |  |  |
| 18 | `LUMSUMORPER` | INTEGER | NOT NULL |  |  |  |
| 19 | `LUMPSUMVALUE` | DECIMAL(9,2) |  |  |  |  |
| 20 | `PERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 21 | `NEWBASIC` | DECIMAL(11,2) |  |  |  |  |
| 22 | `OLDDESIGNATION` | CHAR(6) |  |  |  |  |
| 23 | `NEWDESIGNATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 24 | `NEWDESIGNATIONCODE` | CHAR(6) |  |  |  |  |
| 25 | `OLDSECTION` | CHAR(6) |  |  |  |  |
| 26 | `NEWSECTIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 27 | `NEWSECTIONCODE` | CHAR(6) |  |  |  |  |
| 28 | `OLDMACHINETYPE` | CHAR(6) |  |  |  |  |
| 29 | `NEWMACHINETYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 30 | `NEWMACHINETYPECODE` | CHAR(6) |  |  |  |  |
| 31 | `OLDMACHINENO` | CHAR(6) |  |  |  |  |
| 32 | `NEWMACHINENOICSTABLECODE` | CHAR(4) |  |  |  |  |
| 33 | `NEWMACHINENOCODE` | CHAR(6) |  |  |  |  |
| 34 | `AUTHORIZEFLAG` | INTEGER | NOT NULL |  |  |  |
| 35 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 36 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 37 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 38 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 39 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 40 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 41 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKINCREMENTENTRYREQUESTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CHOOSE,
       t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.INCREMENTNO,
       t.CATEGORYICSTABLECODE,
       t.CATEGORYCODE,
       t.SUBCTGSUBCATEGORYICSTABLECODE,
       t.SUBCATEGORYSUBCATEGORYCODE,
       t.DIVISIONCODE,
       t.FACTORYCOMPANYCODE,
       t.FACTORYCODE,
       t.DEPARTMENTDEPARTMENTCODE
FROM   DB2ADMIN.WRKINCREMENTENTRYREQUEST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
