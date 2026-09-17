# DB2ADMIN.SALESDOCUMENTCOMMISSION

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `SALESDOCUMENTCOMPANYCODE`, `SALDOCPROVISIONALCOUNTERCODE`, `SALESDOCUMENTPROVISIONALCODE`, `AGENTCODE`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 40138

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESDOCUMENTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SALDOCPROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SALESDOCUMENTPROVISIONALCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
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
| `AGENT_AGENT` | `SALESDOCUMENTCOMPANYCODE`, `AGENTCODE` | [`AGENT`](../CORE_MASTER/AGENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESDOCUMENTCOMMISSION.SALESDOCUMENTCOMPANYCODE = AGENT.COMPANYCODE AND SALESDOCUMENTCOMMISSION.AGENTCODE = AGENT.CODE` |
| `CURRENCY_COMMISSIONCURRENCY` | `COMMISSIONCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `SALESDOCUMENTCOMMISSION.COMMISSIONCURRENCYCODE = CURRENCY.CODE` |
| `LOGREASON_LOGREASON` | `SALESDOCUMENTCOMPANYCODE`, `LOGREASONCODE` | [`LOGREASON`](../LOGISTICS/LOGREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESDOCUMENTCOMMISSION.SALESDOCUMENTCOMPANYCODE = LOGREASON.COMPANYCODE AND SALESDOCUMENTCOMMISSION.LOGREASONCODE = LOGREASON.CODE` |
| `SALESDOCUMENT_COMMISSION` | `SALESDOCUMENTCOMPANYCODE`, `SALDOCPROVISIONALCOUNTERCODE`, `SALESDOCUMENTPROVISIONALCODE` | [`SALESDOCUMENT`](../SALES/SALESDOCUMENT.md) | `COMPANYCODE`, `PROVISIONALCOUNTERCODE`, `PROVISIONALCODE` | RESTRICT | `SALESDOCUMENTCOMMISSION.SALESDOCUMENTCOMPANYCODE = SALESDOCUMENT.COMPANYCODE AND SALESDOCUMENTCOMMISSION.SALDOCPROVISIONALCOUNTERCODE = SALESDOCUMENT.PROVISIONALCOUNTERCODE AND SALESDOCUMENTCOMMISSION.SALESDOCUMENTPROVISIONALCODE = SALESDOCUMENT.PROVISIONALCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESDOCUMENTCOMMISSIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SALESDOCUMENTCOMPANYCODE,
       t.SALDOCPROVISIONALCOUNTERCODE,
       t.SALESDOCUMENTPROVISIONALCODE,
       t.AGENTCODE,
       t.NUMBERID,
       t.SEQUENCE,
       t.COMMISSIONTYPE,
       t.COMMISSIONVALUE,
       t.COMMISSIONCURRENCYCODE,
       t.COMMISSIONSIGN,
       t.CALCULATIONTYPE,
       t.AMOUNTCALCULATIONTYPE
FROM   DB2ADMIN.SALESDOCUMENTCOMMISSION t
FETCH FIRST 100 ROWS ONLY;
```
