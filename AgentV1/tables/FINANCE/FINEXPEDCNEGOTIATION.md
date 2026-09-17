# DB2ADMIN.FINEXPEDCNEGOTIATION

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `FINEXPEDCHARGESCOMPANYCODE`, `FINEXPEDCHARGESCODE`, `NEGOTIATIONCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 176400

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINEXPEDCHARGESCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINEXPEDCHARGESCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `NEGOTIATIONTYPE` | CHAR(1) |  |  |  |  |
| 3 | `NEGOTIATIONCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `REFERENCENUM` | CHAR(15) |  |  |  |  |
| 5 | `REFERENCEDATE` | DATE |  |  |  |  |
| 6 | `ADJUSTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 7 | `RATEDIFF` | DECIMAL(18,5) |  |  |  |  |
| 8 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `BANKCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 10 | `POSTED` | SMALLINT | NOT NULL |  |  |  |
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
| `FINEXPEDCHARGES_NEGOTIATION` | `FINEXPEDCHARGESCOMPANYCODE`, `FINEXPEDCHARGESCODE` | [`FINEXPEDCHARGES`](../FINANCE/FINEXPEDCHARGES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINEXPEDCNEGOTIATION.FINEXPEDCHARGESCOMPANYCODE = FINEXPEDCHARGES.COMPANYCODE AND FINEXPEDCNEGOTIATION.FINEXPEDCHARGESCODE = FINEXPEDCHARGES.CODE` |
| `FINEXPNEGOTIATION_NEGOTIATION` | `FINEXPEDCHARGESCOMPANYCODE`, `NEGOTIATIONCODE` | [`FINEXPNEGOTIATION`](../FINANCE/FINEXPNEGOTIATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINEXPEDCNEGOTIATION.FINEXPEDCHARGESCOMPANYCODE = FINEXPNEGOTIATION.COMPANYCODE AND FINEXPEDCNEGOTIATION.NEGOTIATIONCODE = FINEXPNEGOTIATION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINEXPEDCNEGOTIATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINEXPEDCHARGESCOMPANYCODE,
       t.FINEXPEDCHARGESCODE,
       t.NEGOTIATIONTYPE,
       t.NEGOTIATIONCODE,
       t.REFERENCENUM,
       t.REFERENCEDATE,
       t.ADJUSTEDAMOUNT,
       t.RATEDIFF,
       t.VALUE,
       t.BANKCHARGES,
       t.POSTED,
       t.CREATIONDATETIME
FROM   DB2ADMIN.FINEXPEDCNEGOTIATION t
FETCH FIRST 100 ROWS ONLY;
```
