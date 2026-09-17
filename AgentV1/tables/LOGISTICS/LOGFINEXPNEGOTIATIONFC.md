# DB2ADMIN.LOGFINEXPNEGOTIATIONFC

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 35
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 202825

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BANKREFERENCENO` | CHAR(30) |  |  |  |  |
| 2 | `NEGOTIATIONCODE` | CHAR(5) | NOT NULL |  |  |  |
| 3 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 4 | `DUEDATE` | DATE |  |  |  |  |
| 5 | `POSTINGDATE` | DATE |  |  |  |  |
| 6 | `RATE` | DECIMAL(18,5) |  |  |  |  |
| 7 | `FINDOCUMENTBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 8 | `FINDOCUMENTFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 9 | `FINDOCDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 10 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 11 | `FINDOCUMENTCODE` | CHAR(15) |  |  |  |  |
| 12 | `UNUTILISED` | DECIMAL(18,5) |  |  |  |  |
| 13 | `ADJFORTHISBILL` | DECIMAL(18,5) |  |  |  |  |
| 14 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 15 | `FCNO` | CHAR(5) | NOT NULL |  |  |  |
| 16 | `PCGLACCOUNTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 17 | `PCGLACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 18 | `BANKCHARGESGLACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 19 | `SPOTRATE` | INTEGER | NOT NULL |  |  |  |
| 20 | `USDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 21 | `INRVALUE` | DECIMAL(18,5) |  |  |  |  |
| 22 | `SPOTRATEA` | INTEGER | NOT NULL |  |  |  |
| 23 | `USDVALUEA` | DECIMAL(18,5) |  |  |  |  |
| 24 | `INRVALUEA` | DECIMAL(18,5) |  |  |  |  |
| 25 | `USDVALUEC` | DECIMAL(18,5) |  |  |  |  |
| 26 | `INRVALUEC` | DECIMAL(18,5) |  |  |  |  |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 28 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 29 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 30 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 31 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 32 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 33 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 34 | `BCHARGESGLACCOUNTCOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINEXPNEGOTIATIONFC.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BANKREFERENCENO,
       t.NEGOTIATIONCODE,
       t.BUSINESSUNITCODE,
       t.DUEDATE,
       t.POSTINGDATE,
       t.RATE,
       t.FINDOCUMENTBUSINESSUNITCODE,
       t.FINDOCUMENTFINANCIALYEARCODE,
       t.FINDOCDOCUMENTTEMPLATECODE,
       t.FINDOCSTATISTICALGROUPCODE,
       t.FINDOCUMENTCODE
FROM   DB2ADMIN.LOGFINEXPNEGOTIATIONFC t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
