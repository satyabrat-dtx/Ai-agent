# DB2ADMIN.VPMNOWADDITIONALDATA

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `VPCUSTOMIZEDOPTIONSCOMPANYCODE`, `ENTITYNAME`, `ADNAME`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 120513

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `VPCUSTOMIZEDOPTIONSCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ENTITYNAME` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ADNAME` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 4 | `LABEL` | CHAR(50) |  |  |  |  |
| 5 | `READONLY` | INTEGER | NOT NULL |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADADDITIONALDATA_AD` | `ENTITYNAME`, `ADNAME` | [`ADADDITIONALDATA`](../CORE_MASTER/ADADDITIONALDATA.md) | `ENTITYNAME`, `NAME` | RESTRICT | `VPMNOWADDITIONALDATA.ENTITYNAME = ADADDITIONALDATA.ENTITYNAME AND VPMNOWADDITIONALDATA.ADNAME = ADADDITIONALDATA.NAME` |
| `ADENTITY_ENTITY` | `ENTITYNAME` | [`ADENTITY`](../LOCALIZATION/ADENTITY.md) | `NAME` | RESTRICT | `VPMNOWADDITIONALDATA.ENTITYNAME = ADENTITY.NAME` |
| `VPCUSTOMIZEDOPTIONS_VPMADDATA` | `VPCUSTOMIZEDOPTIONSCOMPANYCODE` | [`VPCUSTOMIZEDOPTIONS`](../PLATFORM/VPCUSTOMIZEDOPTIONS.md) | `COMPANYCODE` | RESTRICT | `VPMNOWADDITIONALDATA.VPCUSTOMIZEDOPTIONSCOMPANYCODE = VPCUSTOMIZEDOPTIONS.COMPANYCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `VPMNOWADDITIONALDATAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.VPCUSTOMIZEDOPTIONSCOMPANYCODE,
       t.ENTITYNAME,
       t.ADNAME,
       t.SEQUENCE,
       t.LABEL,
       t.READONLY,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.VPMNOWADDITIONALDATA t
FETCH FIRST 100 ROWS ONLY;
```
