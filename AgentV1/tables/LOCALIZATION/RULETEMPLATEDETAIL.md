# DB2ADMIN.RULETEMPLATEDETAIL

- **Module**: `LOCALIZATION` (low confidence — FK neighbourhood: 1 of 1 related tables are LOCALIZATION)
- **Roles**: `business_data`
- **Columns**: 49
- **Primary key**: `RULETEMPLATEHEADERCOMPANYCODE`, `RULETEMPLATEHEADERCODE`, `IDENTIFIER`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 80728

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RULETEMPLATEHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `RULETEMPLATEHEADERCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `IDENTIFIER` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 3 | `SEQUENCE` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 4 | `ENTITYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `ENTITYTYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `ABSUIXMLABSUIXMLPATH` | VARCHAR(50) |  |  |  |  |
| 7 | `ABSUIXMLABSUIXMLNAME` | VARCHAR(54) |  |  |  |  |
| 8 | `ABSUIXMLNAME` | VARCHAR(120) |  |  |  |  |
| 9 | `ADENTITYNAME` | CHAR(50) |  | FK | foreign_key |  |
| 10 | `ADDATANAME` | CHAR(50) |  |  |  |  |
| 11 | `ADFIELDNAME` | VARCHAR(120) |  |  |  |  |
| 12 | `ATTRIBUTETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `ATTRIBUTETYPEVALUE` | INTEGER | NOT NULL |  |  |  |
| 14 | `OUTPUTFIELDABSUIXMLPATH` | VARCHAR(50) |  |  |  |  |
| 15 | `OUTPUTFIELDABSUIXMLNAME` | VARCHAR(54) |  |  |  |  |
| 16 | `OUTPUTFIELDNAME` | VARCHAR(120) |  |  |  |  |
| 17 | `USERDEFINEDID` | CHAR(50) |  |  |  |  |
| 18 | `LABEL` | CHAR(120) | NOT NULL |  |  |  |
| 19 | `COMPAREOPERATOR` | INTEGER | NOT NULL |  |  |  |
| 20 | `LIKEINIT` | INTEGER | NOT NULL |  |  |  |
| 21 | `LIKELENGTH` | INTEGER | NOT NULL |  |  |  |
| 22 | `JAVANAME` | VARCHAR(100) |  |  |  |  |
| 23 | `SQLTYPE` | CHAR(50) |  |  |  |  |
| 24 | `HTMLTYPE` | CHAR(20) |  |  |  |  |
| 25 | `MAXLENGTH` | DECIMAL(10,0) |  |  |  |  |
| 26 | `HTMLSIZE` | DECIMAL(3,0) |  |  |  |  |
| 27 | `HTMLROWS` | DECIMAL(3,0) |  |  |  |  |
| 28 | `EDITMASK` | CHAR(50) |  |  |  |  |
| 29 | `NBRDECIMALS` | DECIMAL(3,0) |  |  |  |  |
| 30 | `NBRINTEGERS` | DECIMAL(10,0) |  |  |  |  |
| 31 | `REFERENCED` | VARCHAR(100) |  |  |  |  |
| 32 | `OTHERKEYS` | VARCHAR(1500) |  |  |  |  |
| 33 | `OPTIONS` | VARCHAR(2000) |  |  |  |  |
| 34 | `DFTVALUE` | CHAR(50) |  |  |  |  |
| 35 | `RANGELIMITTYPE` | INTEGER | NOT NULL |  |  |  |
| 36 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 37 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 38 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 39 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 40 | `REALREFERENCED` | VARCHAR(100) |  |  |  |  |
| 41 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 42 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 43 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 44 | `OUTPUTENTITYCODE` | CHAR(3) |  |  |  |  |
| 45 | `OUTPUTTEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 46 | `OUTPUTIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 47 | `OUTPUTADFIELDNAME` | VARCHAR(120) |  |  |  |  |
| 48 | `CANNOTBEEMPTY` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADENTITY_ADENTITY` | `ADENTITYNAME` | [`ADENTITY`](../LOCALIZATION/ADENTITY.md) | `NAME` | RESTRICT | `RULETEMPLATEDETAIL.ADENTITYNAME = ADENTITY.NAME` |
| `RULEENTITY_ENTITY` | `ENTITYCODE` | [`RULEENTITY`](../PLATFORM/RULEENTITY.md) | `CODE` | RESTRICT | `RULETEMPLATEDETAIL.ENTITYCODE = RULEENTITY.CODE` |
| `RULETEMPLATEHEADER_DETAIL` | `RULETEMPLATEHEADERCOMPANYCODE`, `RULETEMPLATEHEADERCODE` | [`RULETEMPLATEHEADER`](../LOCALIZATION/RULETEMPLATEHEADER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RULETEMPLATEDETAIL.RULETEMPLATEHEADERCOMPANYCODE = RULETEMPLATEHEADER.COMPANYCODE AND RULETEMPLATEDETAIL.RULETEMPLATEHEADERCODE = RULETEMPLATEHEADER.CODE` |
| `RULETEMPLATEHEADER_OUTPUTTEMPLATE` | `RULETEMPLATEHEADERCOMPANYCODE`, `OUTPUTTEMPLATECODE` | [`RULETEMPLATEHEADER`](../LOCALIZATION/RULETEMPLATEHEADER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RULETEMPLATEDETAIL.RULETEMPLATEHEADERCOMPANYCODE = RULETEMPLATEHEADER.COMPANYCODE AND RULETEMPLATEDETAIL.OUTPUTTEMPLATECODE = RULETEMPLATEHEADER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RULETEMPLATEDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RULETEMPLATEHEADERCOMPANYCODE,
       t.RULETEMPLATEHEADERCODE,
       t.IDENTIFIER,
       t.SEQUENCE,
       t.ENTITYCODE,
       t.ENTITYTYPE,
       t.ABSUIXMLABSUIXMLPATH,
       t.ABSUIXMLABSUIXMLNAME,
       t.ABSUIXMLNAME,
       t.ADENTITYNAME,
       t.ADDATANAME,
       t.ADFIELDNAME
FROM   DB2ADMIN.RULETEMPLATEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
