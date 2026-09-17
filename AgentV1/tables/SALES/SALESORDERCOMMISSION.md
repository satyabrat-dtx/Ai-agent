# DB2ADMIN.SALESORDERCOMMISSION

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `SALESORDERCOMPANYCODE`, `SALESORDERCOUNTERCODE`, `SALESORDERCODE`, `AGENTCODE`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 40617

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SALESORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SALESORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `AGENTCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 5 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 6 | `COMMISSIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `COMMISSIONVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 8 | `COMMISSIONCURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 9 | `COMMISSIONSIGN` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 12 | `COMMISSIONCREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 13 | `DEFSALCMSDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 14 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 15 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 16 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 17 | `LOGREASONCODE` | CHAR(2) |  | FK | foreign_key |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 23 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 24 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `AGENT_AGENT` | `SALESORDERCOMPANYCODE`, `AGENTCODE` | [`AGENT`](../CORE_MASTER/AGENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESORDERCOMMISSION.SALESORDERCOMPANYCODE = AGENT.COMPANYCODE AND SALESORDERCOMMISSION.AGENTCODE = AGENT.CODE` |
| `CURRENCY_COMMISSIONCURRENCY` | `COMMISSIONCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `SALESORDERCOMMISSION.COMMISSIONCURRENCYCODE = CURRENCY.CODE` |
| `LOGREASON_LOGREASON` | `SALESORDERCOMPANYCODE`, `LOGREASONCODE` | [`LOGREASON`](../LOGISTICS/LOGREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESORDERCOMMISSION.SALESORDERCOMPANYCODE = LOGREASON.COMPANYCODE AND SALESORDERCOMMISSION.LOGREASONCODE = LOGREASON.CODE` |
| `SALESORDER_COMMISSION` | `SALESORDERCOMPANYCODE`, `SALESORDERCOUNTERCODE`, `SALESORDERCODE` | [`SALESORDER`](../SALES/SALESORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `SALESORDERCOMMISSION.SALESORDERCOMPANYCODE = SALESORDER.COMPANYCODE AND SALESORDERCOMMISSION.SALESORDERCOUNTERCODE = SALESORDER.COUNTERCODE AND SALESORDERCOMMISSION.SALESORDERCODE = SALESORDER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESORDERCOMMISSIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SALESORDERCOMPANYCODE,
       t.SALESORDERCOUNTERCODE,
       t.SALESORDERCODE,
       t.AGENTCODE,
       t.NUMBERID,
       t.SEQUENCE,
       t.COMMISSIONTYPE,
       t.COMMISSIONVALUE,
       t.COMMISSIONCURRENCYCODE,
       t.COMMISSIONSIGN,
       t.CALCULATIONTYPE,
       t.AMOUNTCALCULATIONTYPE
FROM   DB2ADMIN.SALESORDERCOMMISSION t
FETCH FIRST 100 ROWS ONLY;
```
