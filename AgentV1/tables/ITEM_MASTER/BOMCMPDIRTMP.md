# DB2ADMIN.BOMCMPDIRTMP

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'BOM')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `BOMCMP`, `BOMNID`, `BOMSEQ`, `BOMSS`, `DIRECTIVETEMPLATECODE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 198860

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BOMCMP` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `BOMNID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `BOMSEQ` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `BOMSS` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `DIRECTIVETEMPLATECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BOMCOMPONENT_DIRECTIVETEMPLATE` | `BOMCMP`, `BOMNID`, `BOMSEQ`, `BOMSS` | [`BOMCOMPONENT`](../ITEM_MASTER/BOMCOMPONENT.md) | `BILLOFMATERIALCOMPANYCODE`, `BILLOFMATERIALNUMBERID`, `SEQUENCE`, `SUBSEQUENCE` | RESTRICT | `BOMCMPDIRTMP.BOMCMP = BOMCOMPONENT.BILLOFMATERIALCOMPANYCODE AND BOMCMPDIRTMP.BOMNID = BOMCOMPONENT.BILLOFMATERIALNUMBERID AND BOMCMPDIRTMP.BOMSEQ = BOMCOMPONENT.SEQUENCE AND BOMCMPDIRTMP.BOMSS = BOMCOMPONENT.SUBSEQUENCE` |
| `DIRECTIVETEMPLATE_DIRECTIVETEMPLATE` | `BOMCMP`, `DIRECTIVETEMPLATECODE` | [`DIRECTIVETEMPLATE`](../ITEM_MASTER/DIRECTIVETEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BOMCMPDIRTMP.BOMCMP = DIRECTIVETEMPLATE.COMPANYCODE AND BOMCMPDIRTMP.DIRECTIVETEMPLATECODE = DIRECTIVETEMPLATE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `BOMCMPDIRTMP_VALUE` | [`BOMCMPDIRVAL`](../ITEM_MASTER/BOMCMPDIRVAL.md) | `BOMCMP`, `BOMNID`, `BOMSEQ`, `BOMSS`, `BOMCMPDTM` | `BOMCMPDIRVAL.BOMCMP = BOMCMPDIRTMP.BOMCMP AND BOMCMPDIRVAL.BOMNID = BOMCMPDIRTMP.BOMNID AND BOMCMPDIRVAL.BOMSEQ = BOMCMPDIRTMP.BOMSEQ AND BOMCMPDIRVAL.BOMSS = BOMCMPDIRTMP.BOMSS AND BOMCMPDIRVAL.BOMCMPDTM = BOMCMPDIRTMP.DIRECTIVETEMPLATECODE` |

## Indexes

- `BOMCMPDIRTMPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.BOMCMP,
       t.BOMNID,
       t.BOMSEQ,
       t.BOMSS,
       t.DIRECTIVETEMPLATECODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.BOMCMPDIRTMP t
FETCH FIRST 100 ROWS ONLY;
```
