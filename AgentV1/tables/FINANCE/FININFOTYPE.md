# DB2ADMIN.FININFOTYPE

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `CODE`
- **FK degree**: referenced by 9 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 101589

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(2) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 9

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FININFOTYPE_INFOTYPE` | [`FINPERIODBALANCES`](../FINANCE/FINPERIODBALANCES.md) | `INFOTYPECODE` | `FINPERIODBALANCES.INFOTYPECODE = FININFOTYPE.CODE` |
| `FININFOTYPE_INFOTYPE` | [`FINVOUHEADER`](../FINANCE/FINVOUHEADER.md) | `INFOTYPECODE` | `FINVOUHEADER.INFOTYPECODE = FININFOTYPE.CODE` |
| `FININFOTYPE_INFOTYPE` | [`VOUCHERCUSTOMIZEDOPTIONS`](../FINANCE/VOUCHERCUSTOMIZEDOPTIONS.md) | `INFOTYPECODE` | `VOUCHERCUSTOMIZEDOPTIONS.INFOTYPECODE = FININFOTYPE.CODE` |
| `FININFOTYPE_INFOTYPE` | [`ASSETGROUP`](../FINANCE/ASSETGROUP.md) | `INFOTYPECODE` | `ASSETGROUP.INFOTYPECODE = FININFOTYPE.CODE` |
| `FININFOTYPE_INFOTYPE` | [`ASSETMASTER`](../FINANCE/ASSETMASTER.md) | `INFOTYPECODE` | `ASSETMASTER.INFOTYPECODE = FININFOTYPE.CODE` |
| `FININFOTYPE_INFOTYPE` | [`FINVOUCHERTEMPLATE`](../FINANCE/FINVOUCHERTEMPLATE.md) | `INFOTYPECODE` | `FINVOUCHERTEMPLATE.INFOTYPECODE = FININFOTYPE.CODE` |
| `FININFOTYPE_INFOTYPE` | [`PERIODMASTER`](../FINANCE/PERIODMASTER.md) | `INFOTYPECODE` | `PERIODMASTER.INFOTYPECODE = FININFOTYPE.CODE` |
| `FININFOTYPE_INFOTYPE` | [`PAYMENTEXECUTION`](../FINANCE/PAYMENTEXECUTION.md) | `INFOTYPECODE` | `PAYMENTEXECUTION.INFOTYPECODE = FININFOTYPE.CODE` |
| `FININFOTYPE_INFOTYPE` | [`PAYMENTPROPOSAL`](../FINANCE/PAYMENTPROPOSAL.md) | `INFOTYPECODE` | `PAYMENTPROPOSAL.INFOTYPECODE = FININFOTYPE.CODE` |

## Indexes

- `FININFOTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.FININFOTYPE t
FETCH FIRST 100 ROWS ONLY;
```
