# DB2ADMIN.PAYMENTEXECUTION

- **Module**: `FINANCE` (low confidence — FK neighbourhood: 1 of 1 related tables are FINANCE)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `CODE`, `COMPANYBANKCODE`, `PAYMENTTYPECODE`, `CURRENCYCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 104208

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `CODE` | DECIMAL(15,0) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `COMPANYBANKCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 4 | `PAYMENTTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `CURRENCYCODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 6 | `PAYMENTAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 7 | `PAYMENTAMOUNTCURRENCY` | DECIMAL(17,2) |  |  |  |  |
| 8 | `PAYMENTDISCOUNTAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 9 | `PAYMENTDISCOUNTAMOUNTCURRENCY` | DECIMAL(17,2) |  |  |  |  |
| 10 | `NBROFTRANSACTION` | INTEGER | NOT NULL |  |  |  |
| 11 | `INFOTYPECODE` | CHAR(2) |  | FK | foreign_key |  |
| 12 | `INTERNALVOUCHERCODE` | DECIMAL(15,0) |  |  |  |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PAYMENTEXECUTION.COMPANYCODE = COMPANY.CODE` |
| `FININFOTYPE_INFOTYPE` | `INFOTYPECODE` | [`FININFOTYPE`](../FINANCE/FININFOTYPE.md) | `CODE` | RESTRICT | `PAYMENTEXECUTION.INFOTYPECODE = FININFOTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PAYMENTEXECUTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CODE,
       t.COMPANYBANKCODE,
       t.PAYMENTTYPECODE,
       t.CURRENCYCODE,
       t.PAYMENTAMOUNT,
       t.PAYMENTAMOUNTCURRENCY,
       t.PAYMENTDISCOUNTAMOUNT,
       t.PAYMENTDISCOUNTAMOUNTCURRENCY,
       t.NBROFTRANSACTION,
       t.INFOTYPECODE
FROM   DB2ADMIN.PAYMENTEXECUTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
