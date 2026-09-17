# DB2ADMIN.FIRCREALISATION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `REALSNNO`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 182467

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `REALSNNO` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `REALSNDATE` | DATE |  |  |  |  |
| 3 | `FIRCSUBMISSIONNO` | CHAR(20) |  |  |  |  |
| 4 | `FIRCSUBDT` | DATE |  |  |  |  |
| 5 | `FIRCNO` | CHAR(20) |  |  |  |  |
| 6 | `FIRCDT` | DATE |  |  |  |  |
| 7 | `BUYERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 8 | `BUYERCUSTOMERSUPPLIERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 9 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 10 | `FIRCAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `FIRCREALISATION.CURRENCYCODE = CURRENCY.CODE` |
| `ORDERPARTNER_BUYER` | `COMPANYCODE`, `BUYERCUSTOMERSUPPLIERTYPE`, `BUYERCUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `FIRCREALISATION.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND FIRCREALISATION.BUYERCUSTOMERSUPPLIERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND FIRCREALISATION.BUYERCUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FIRCREALISATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.REALSNNO,
       t.REALSNDATE,
       t.FIRCSUBMISSIONNO,
       t.FIRCSUBDT,
       t.FIRCNO,
       t.FIRCDT,
       t.BUYERCUSTOMERSUPPLIERTYPE,
       t.BUYERCUSTOMERSUPPLIERCODE,
       t.CURRENCYCODE,
       t.FIRCAMOUNT,
       t.CREATIONDATETIME
FROM   DB2ADMIN.FIRCREALISATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
