# DB2ADMIN.EINVOICEOTHERDATA

- **Module**: `EINVOICING` (high confidence — table name starts with 'EINVOIC')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `OTHERDATAID`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 237179

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EINVOICEHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EINVOICEHEADERUNIQUEID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EINVOICEBODYID` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `OTHERDATAID` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `SALESDOCUMENTLINETAX` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 5 | `TAXNATURECODE` | CHAR(4) |  | FK | foreign_key |  |
| 6 | `CHARGES` | DECIMAL(14,2) |  |  |  |  |
| 7 | `TAXABLEAMOUNT` | DECIMAL(14,2) | NOT NULL |  |  |  |
| 8 | `TAXAMOUNT` | DECIMAL(14,2) | NOT NULL |  |  |  |
| 9 | `PAYABILITYCODE` | CHAR(1) |  | FK | foreign_key |  |
| 10 | `TAXLAWREFERENCE` | VARCHAR(200) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EINVOICEBODY_OTHERDATA` | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID` | [`EINVOICEBODY`](../EINVOICING/EINVOICEBODY.md) | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `BODYID` | RESTRICT | `EINVOICEOTHERDATA.EINVOICEHEADERCOMPANYCODE = EINVOICEBODY.EINVOICEHEADERCOMPANYCODE AND EINVOICEOTHERDATA.EINVOICEHEADERUNIQUEID = EINVOICEBODY.EINVOICEHEADERUNIQUEID AND EINVOICEOTHERDATA.EINVOICEBODYID = EINVOICEBODY.BODYID` |
| `PAYABILITY_PAYABILITY` | `PAYABILITYCODE` | [`PAYABILITY`](../EINVOICING/PAYABILITY.md) | `CODE` | RESTRICT | `EINVOICEOTHERDATA.PAYABILITYCODE = PAYABILITY.CODE` |
| `TAXNATURE_TAXNATURE` | `TAXNATURECODE` | [`TAXNATURE`](../EINVOICING/TAXNATURE.md) | `CODE` | RESTRICT | `EINVOICEOTHERDATA.TAXNATURECODE = TAXNATURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EINVOICEOTHERDATAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EINVOICEHEADERCOMPANYCODE,
       t.EINVOICEHEADERUNIQUEID,
       t.EINVOICEBODYID,
       t.OTHERDATAID,
       t.SALESDOCUMENTLINETAX,
       t.TAXNATURECODE,
       t.CHARGES,
       t.TAXABLEAMOUNT,
       t.TAXAMOUNT,
       t.PAYABILITYCODE,
       t.TAXLAWREFERENCE,
       t.CREATIONDATETIME
FROM   DB2ADMIN.EINVOICEOTHERDATA t
FETCH FIRST 100 ROWS ONLY;
```
