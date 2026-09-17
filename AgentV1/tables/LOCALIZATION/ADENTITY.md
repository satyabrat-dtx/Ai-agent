# DB2ADMIN.ADENTITY

- **Module**: `LOCALIZATION` (low confidence — FK neighbourhood: 1 of 1 related tables are LOCALIZATION)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `NAME`
- **FK degree**: referenced by 9 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 3812

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `NAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `PACKAGE` | CHAR(50) | NOT NULL |  |  |  |
| 2 | `HANDLEADDITIONALDATA` | INTEGER | NOT NULL |  |  |  |
| 3 | `TOLORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 4 | `ADPOLICYCODE` | CHAR(20) |  |  |  |  |
| 5 | `ADPRECREATEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 6 | `COMPANYCODENAME` | CHAR(80) |  |  |  |  |
| 7 | `ITEMTYPECODENAME` | CHAR(60) |  |  |  |  |
| 8 | `JNDINAME` | VARCHAR(100) | NOT NULL |  |  |  |
| 9 | `JNDISHAREDNAME` | VARCHAR(100) |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 15 | `VPMENABLED` | SMALLINT | NOT NULL |  |  |  |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 9

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ADENTITY_ENTITY` | [`ADATTRIBUTE`](../LOCALIZATION/ADATTRIBUTE.md) | `ENTITYNAME` | `ADATTRIBUTE.ENTITYNAME = ADENTITY.NAME` |
| `ADENTITY_ENTITY` | [`ADTOEXPORT`](../OTHER/ADTOEXPORT.md) | `ENTITYNAME` | `ADTOEXPORT.ENTITYNAME = ADENTITY.NAME` |
| `ADENTITY_TOLENTITY` | [`TOLENTITIES`](../LOCALIZATION/TOLENTITIES.md) | `TOLENTITYNAME` | `TOLENTITIES.TOLENTITYNAME = ADENTITY.NAME` |
| `ADENTITY_ADENTITY` | [`RULEENTITYATTRIBUTE`](../LOCALIZATION/RULEENTITYATTRIBUTE.md) | `ADENTITYNAME` | `RULEENTITYATTRIBUTE.ADENTITYNAME = ADENTITY.NAME` |
| `ADENTITY_ENTITY` | [`ADADDITIONALDATA`](../CORE_MASTER/ADADDITIONALDATA.md) | `ENTITYNAME` | `ADADDITIONALDATA.ENTITYNAME = ADENTITY.NAME` |
| `ADENTITY_ADENTITY` | [`RULETEMPLATEDETAIL`](../LOCALIZATION/RULETEMPLATEDETAIL.md) | `ADENTITYNAME` | `RULETEMPLATEDETAIL.ADENTITYNAME = ADENTITY.NAME` |
| `ADENTITY_CSRMTOLENTITY` | [`CSRMTE`](../LOCALIZATION/CSRMTE.md) | `CSRMTOLENTITYNAME` | `CSRMTE.CSRMTOLENTITYNAME = ADENTITY.NAME` |
| `ADENTITY_ENTITY` | [`VPMNOWADDITIONALDATA`](../OTHER/VPMNOWADDITIONALDATA.md) | `ENTITYNAME` | `VPMNOWADDITIONALDATA.ENTITYNAME = ADENTITY.NAME` |
| `ADENTITY_TOLENTITY` | [`NETTOLENTITIES`](../LOCALIZATION/NETTOLENTITIES.md) | `TOLENTITYNAME` | `NETTOLENTITIES.TOLENTITYNAME = ADENTITY.NAME` |

## Indexes

- `ADENTITYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.NAME,
       t.PACKAGE,
       t.HANDLEADDITIONALDATA,
       t.TOLORDERTYPE,
       t.ADPOLICYCODE,
       t.ADPRECREATEPOLICYCODE,
       t.COMPANYCODENAME,
       t.ITEMTYPECODENAME,
       t.JNDINAME,
       t.JNDISHAREDNAME,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.ADENTITY t
FETCH FIRST 100 ROWS ONLY;
```
