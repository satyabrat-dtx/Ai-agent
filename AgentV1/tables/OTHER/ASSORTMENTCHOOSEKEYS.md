# DB2ADMIN.ASSORTMENTCHOOSEKEYS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `ASRCHSKEYSHEADERCOMPANYCODE`, `ASRCHOOSEKEYSHEADERORDERTYPE`, `ASSORTMENTCHOOSEKEYSHEADERCODE`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 4471

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ASRCHSKEYSHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ASRCHOOSEKEYSHEADERORDERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ASSORTMENTCHOOSEKEYSHEADERCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SEQUENCE` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 4 | `DIVISIONCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 5 | `ORDERPARTNERCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `ORDERPARTNERGROUPCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 7 | `FNCORDERPARTNERCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `ORDERCATEGORYCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `AREACONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `STATISTICALGROUPCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `ORDERTEMPLATECODECONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `AGENTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `REFERENCEPARTNERCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 21 | `RFPARTNERGROUPCONTROLLED` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ASSORTMENTCHOOSEKEYSHEADER_ASSORTMENTCHOOSEKEYS` | `ASRCHSKEYSHEADERCOMPANYCODE`, `ASRCHOOSEKEYSHEADERORDERTYPE`, `ASSORTMENTCHOOSEKEYSHEADERCODE` | [`ASSORTMENTCHOOSEKEYSHEADER`](../OTHER/ASSORTMENTCHOOSEKEYSHEADER.md) | `COMPANYCODE`, `ORDERTYPE`, `CODE` | RESTRICT | `ASSORTMENTCHOOSEKEYS.ASRCHSKEYSHEADERCOMPANYCODE = ASSORTMENTCHOOSEKEYSHEADER.COMPANYCODE AND ASSORTMENTCHOOSEKEYS.ASRCHOOSEKEYSHEADERORDERTYPE = ASSORTMENTCHOOSEKEYSHEADER.ORDERTYPE AND ASSORTMENTCHOOSEKEYS.ASSORTMENTCHOOSEKEYSHEADERCODE = ASSORTMENTCHOOSEKEYSHEADER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ASSORTMENTCHOOSEKEYSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ASRCHSKEYSHEADERCOMPANYCODE,
       t.ASRCHOOSEKEYSHEADERORDERTYPE,
       t.ASSORTMENTCHOOSEKEYSHEADERCODE,
       t.SEQUENCE,
       t.DIVISIONCONTROLLED,
       t.ORDERPARTNERCONTROLLED,
       t.ORDERPARTNERGROUPCONTROLLED,
       t.FNCORDERPARTNERCONTROLLED,
       t.ORDERCATEGORYCONTROLLED,
       t.AREACONTROLLED,
       t.STATISTICALGROUPCONTROLLED,
       t.ORDERTEMPLATECODECONTROLLED
FROM   DB2ADMIN.ASSORTMENTCHOOSEKEYS t
FETCH FIRST 100 ROWS ONLY;
```
