# DB2ADMIN.MSESPECMASTERRANGE

- **Module**: `SPECIFICATIONS` (medium confidence — table name starts with 'MSE')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `MSESPECMASTERDEFCOMPANYCODE`, `MSESPECMASTERDEFINITIONCODE`, `CRITERIATYPE`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 198444

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MSESPECMASTERDEFCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `MSESPECMASTERDEFINITIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CRITERIATYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 3 | `SEQUENCE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 4 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `TERMSOFDELIVERYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `PAYMENTMETHODCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `WORKINGCALENDARCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `VALUETYPE` | CHAR(2) |  |  |  |  |
| 10 | `UOMTYPE` | CHAR(2) |  |  |  |  |
| 11 | `VALUEMINIMUM` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 12 | `VALUEMAXIMUM` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 13 | `VALUEOK` | INTEGER | NOT NULL |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `MSESPECMASTERDEFINITION_RANGES` | `MSESPECMASTERDEFCOMPANYCODE`, `MSESPECMASTERDEFINITIONCODE` | [`MSESPECMASTERDEFINITION`](../SPECIFICATIONS/MSESPECMASTERDEFINITION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MSESPECMASTERRANGE.MSESPECMASTERDEFCOMPANYCODE = MSESPECMASTERDEFINITION.COMPANYCODE AND MSESPECMASTERRANGE.MSESPECMASTERDEFINITIONCODE = MSESPECMASTERDEFINITION.CODE` |
| `PAYMENTMETHOD_PAYMENTMETHOD` | `PAYMENTMETHODCOMPANYCODE`, `PAYMENTMETHODCODE` | [`PAYMENTMETHOD`](../CORE_MASTER/PAYMENTMETHOD.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MSESPECMASTERRANGE.PAYMENTMETHODCOMPANYCODE = PAYMENTMETHOD.COMPANYCODE AND MSESPECMASTERRANGE.PAYMENTMETHODCODE = PAYMENTMETHOD.CODE` |
| `TERMSOFDELIVERY_TERMSOFDELIVERY` | `TERMSOFDELIVERYCOMPANYCODE`, `TERMSOFDELIVERYCODE` | [`TERMSOFDELIVERY`](../CORE_MASTER/TERMSOFDELIVERY.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MSESPECMASTERRANGE.TERMSOFDELIVERYCOMPANYCODE = TERMSOFDELIVERY.COMPANYCODE AND MSESPECMASTERRANGE.TERMSOFDELIVERYCODE = TERMSOFDELIVERY.CODE` |
| `WORKINGCALENDAR_WORKINGCALENDAR` | `WORKINGCALENDARCODE` | [`WORKINGCALENDAR`](../CORE_MASTER/WORKINGCALENDAR.md) | `CODE` | RESTRICT | `MSESPECMASTERRANGE.WORKINGCALENDARCODE = WORKINGCALENDAR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MSESPECMASTERRANGEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.MSESPECMASTERDEFCOMPANYCODE,
       t.MSESPECMASTERDEFINITIONCODE,
       t.CRITERIATYPE,
       t.SEQUENCE,
       t.TERMSOFDELIVERYCOMPANYCODE,
       t.TERMSOFDELIVERYCODE,
       t.PAYMENTMETHODCOMPANYCODE,
       t.PAYMENTMETHODCODE,
       t.WORKINGCALENDARCODE,
       t.VALUETYPE,
       t.UOMTYPE,
       t.VALUEMINIMUM
FROM   DB2ADMIN.MSESPECMASTERRANGE t
FETCH FIRST 100 ROWS ONLY;
```
