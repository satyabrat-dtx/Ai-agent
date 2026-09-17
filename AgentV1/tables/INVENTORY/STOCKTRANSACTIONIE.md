# DB2ADMIN.STOCKTRANSACTIONIE

- **Module**: `INVENTORY` (high confidence — table name starts with 'STOCK')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `TRANSACTIONNUMBER`, `TRANSACTIONDETAILNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 147109

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `TRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `TRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `RG23IAEXCISEYEARREGNO` | CHAR(30) |  | FK | foreign_key |  |
| 5 | `RG23IAEXCISEYEARCODE` | CHAR(4) |  | FK | foreign_key |  |
| 6 | `RG23IACODE` | CHAR(15) |  | FK | foreign_key |  |
| 7 | `RG23ICEXCISEYEARREGNO` | CHAR(30) |  | FK | foreign_key |  |
| 8 | `RG23ICEXCISEYEARCODE` | CHAR(4) |  | FK | foreign_key |  |
| 9 | `RG23ICCODE` | CHAR(15) |  | FK | foreign_key |  |
| 10 | `ORDERCOUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `ORDERCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 12 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 13 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 14 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 15 | `ORDERCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 16 | `FLAG` | CHAR(15) |  |  |  |  |
| 17 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `STOCKTRANSACTIONIE.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_ORDERCOUNTER` | `ORDERCOUNTERCOMPANYCODE`, `ORDERCOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `STOCKTRANSACTIONIE.ORDERCOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND STOCKTRANSACTIONIE.ORDERCOUNTERCODE = COUNTER.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `STOCKTRANSACTIONIE.COMPANYCODE = DIVISION.COMPANYCODE AND STOCKTRANSACTIONIE.DIVISIONCODE = DIVISION.CODE` |
| `RG23IA_RG23IA` | `COMPANYCODE`, `RG23IAEXCISEYEARREGNO`, `RG23IAEXCISEYEARCODE`, `RG23IACODE` | [`RG23IA`](../OTHER/RG23IA.md) | `COMPANYCODE`, `EXCISEYEARREGNO`, `EXCISEYEARCODE`, `CODE` | RESTRICT | `STOCKTRANSACTIONIE.COMPANYCODE = RG23IA.COMPANYCODE AND STOCKTRANSACTIONIE.RG23IAEXCISEYEARREGNO = RG23IA.EXCISEYEARREGNO AND STOCKTRANSACTIONIE.RG23IAEXCISEYEARCODE = RG23IA.EXCISEYEARCODE AND STOCKTRANSACTIONIE.RG23IACODE = RG23IA.CODE` |
| `RG23IC_RG23IC` | `COMPANYCODE`, `RG23ICEXCISEYEARREGNO`, `RG23ICEXCISEYEARCODE`, `RG23ICCODE` | [`RG23IC`](../OTHER/RG23IC.md) | `COMPANYCODE`, `EXCISEYEARREGNO`, `EXCISEYEARCODE`, `CODE` | RESTRICT | `STOCKTRANSACTIONIE.COMPANYCODE = RG23IC.COMPANYCODE AND STOCKTRANSACTIONIE.RG23ICEXCISEYEARREGNO = RG23IC.EXCISEYEARREGNO AND STOCKTRANSACTIONIE.RG23ICEXCISEYEARCODE = RG23IC.EXCISEYEARCODE AND STOCKTRANSACTIONIE.RG23ICCODE = RG23IC.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `STOCKTRANSACTIONIEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.TRANSACTIONNUMBER,
       t.TRANSACTIONDETAILNUMBER,
       t.RG23IAEXCISEYEARREGNO,
       t.RG23IAEXCISEYEARCODE,
       t.RG23IACODE,
       t.RG23ICEXCISEYEARREGNO,
       t.RG23ICEXCISEYEARCODE,
       t.RG23ICCODE,
       t.ORDERCOUNTERCOMPANYCODE,
       t.ORDERCOUNTERCODE
FROM   DB2ADMIN.STOCKTRANSACTIONIE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
