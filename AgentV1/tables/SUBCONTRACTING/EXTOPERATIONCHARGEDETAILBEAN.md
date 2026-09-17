# DB2ADMIN.EXTOPERATIONCHARGEDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOPERATION')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 29
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 98547

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `LINEID` | DECIMAL(3,0) |  |  |  |  |
| 3 | `BREAKDOWNCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 4 | `BREAKDOWNUOMCODE` | CHAR(3) |  |  |  |  |
| 5 | `BREAKDOWNLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 6 | `INITIALDATE` | DATE |  |  |  |  |
| 7 | `FINALDATE` | DATE |  |  |  |  |
| 8 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 9 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `CHARGESSUBCODE01` | CHAR(20) |  |  |  |  |
| 11 | `CHARGETYPE` | CHAR(2) |  |  |  |  |
| 12 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `CHARGECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 14 | `SIGN` | CHAR(2) |  |  |  |  |
| 15 | `CALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 16 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 17 | `DIRTYFIELD` | CHAR(20) |  |  |  |  |
| 18 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 19 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 20 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 22 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 24 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 26 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 27 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 28 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `EXTOPERATIONCHARGEDETAILBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `EXTOPERATIONCHARGEDLTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.LINEID,
       t.BREAKDOWNCURRENCYCODE,
       t.BREAKDOWNUOMCODE,
       t.BREAKDOWNLIMIT,
       t.INITIALDATE,
       t.FINALDATE,
       t.PAYMENTMETHODCODE,
       t.ITEMTYPECODE,
       t.CHARGESSUBCODE01,
       t.CHARGETYPE
FROM   DB2ADMIN.EXTOPERATIONCHARGEDETAILBEAN t
FETCH FIRST 100 ROWS ONLY;
```
