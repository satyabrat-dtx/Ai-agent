# DB2ADMIN.SHIPMENTEXCHANGERATE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `CURRENCYCODE`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 123695

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CURRENCYCODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 3 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 4 | `PURCHASERATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 5 | `SALESRATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 6 | `DECIMALPOINT` | INTEGER | NOT NULL |  |  |  |
| 7 | `ROUNDOFF` | INTEGER | NOT NULL |  |  |  |
| 8 | `NUMBEROFDECIMALS` | INTEGER | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SHIPMENTEXCHANGERATE.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `SHIPMENTEXCHANGERATE.CURRENCYCODE = CURRENCY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SHIPMENTEXCHANGERATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CURRENCYCODE,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.PURCHASERATE,
       t.SALESRATE,
       t.DECIMALPOINT,
       t.ROUNDOFF,
       t.NUMBEROFDECIMALS,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.SHIPMENTEXCHANGERATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
