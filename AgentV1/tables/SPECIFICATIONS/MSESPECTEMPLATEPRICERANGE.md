# DB2ADMIN.MSESPECTEMPLATEPRICERANGE

- **Module**: `SPECIFICATIONS` (medium confidence — table name starts with 'MSE')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `MSESPECTEMPLATECOMPANYCODE`, `MSESPECIFICATIONTEMPLATECODE`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 192294

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MSESPECTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `MSESPECIFICATIONTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SEQUENCE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `PAYMENTMETHODCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `FROMVARIATIONPERCENTAGE` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 6 | `TOVARIATIONPERCENTAGE` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `MSESPECIFICATIONTEMPLATE_PRICERANGES` | `MSESPECTEMPLATECOMPANYCODE`, `MSESPECIFICATIONTEMPLATECODE` | [`MSESPECIFICATIONTEMPLATE`](../SPECIFICATIONS/MSESPECIFICATIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MSESPECTEMPLATEPRICERANGE.MSESPECTEMPLATECOMPANYCODE = MSESPECIFICATIONTEMPLATE.COMPANYCODE AND MSESPECTEMPLATEPRICERANGE.MSESPECIFICATIONTEMPLATECODE = MSESPECIFICATIONTEMPLATE.CODE` |
| `PAYMENTMETHOD_PAYMENTMETHOD` | `PAYMENTMETHODCOMPANYCODE`, `PAYMENTMETHODCODE` | [`PAYMENTMETHOD`](../CORE_MASTER/PAYMENTMETHOD.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MSESPECTEMPLATEPRICERANGE.PAYMENTMETHODCOMPANYCODE = PAYMENTMETHOD.COMPANYCODE AND MSESPECTEMPLATEPRICERANGE.PAYMENTMETHODCODE = PAYMENTMETHOD.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MSESPECTEMPLATEPRICERANGEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.MSESPECTEMPLATECOMPANYCODE,
       t.MSESPECIFICATIONTEMPLATECODE,
       t.SEQUENCE,
       t.PAYMENTMETHODCOMPANYCODE,
       t.PAYMENTMETHODCODE,
       t.FROMVARIATIONPERCENTAGE,
       t.TOVARIATIONPERCENTAGE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.MSESPECTEMPLATEPRICERANGE t
FETCH FIRST 100 ROWS ONLY;
```
