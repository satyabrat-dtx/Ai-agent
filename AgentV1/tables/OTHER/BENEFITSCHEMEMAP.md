# DB2ADMIN.BENEFITSCHEMEMAP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `SHIPMENTARTICLECODE`, `PLANTCODE`, `FROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 134962

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `SHIPMENTARTICLECODE` | CHAR(5) | NOT NULL | PK | primary_key |  |
| 3 | `PLANTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `PLANTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 6 | `PRODUCTGROUPSCHEMETYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `PRODUCTGROUPPRODUCTGROUPCODE` | CHAR(3) |  |  |  |  |
| 8 | `PRODUCTGROUPDEPBSRNO` | CHAR(20) |  |  |  |  |
| 9 | `OTHERPRDGROUPSCHEMETYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `OTHERPRDGROUPPRODUCTGROUPCODE` | CHAR(3) |  |  |  |  |
| 11 | `OTHERPRODUCTGROUPDEPBSRNO` | CHAR(20) |  |  |  |  |
| 12 | `FROMDATE` | DATE | NOT NULL | PK | primary_key | Inclusive start of a validity period. |
| 13 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 14 | `REMARK` | VARCHAR(200) |  |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 22 | `SHIPMENTARTICLECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BENEFITSCHEMEMAPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.SHIPMENTARTICLECODE,
       t.PLANTCOMPANYCODE,
       t.PLANTCODE,
       t.PRICE,
       t.PRODUCTGROUPSCHEMETYPECODE,
       t.PRODUCTGROUPPRODUCTGROUPCODE,
       t.PRODUCTGROUPDEPBSRNO,
       t.OTHERPRDGROUPSCHEMETYPECODE,
       t.OTHERPRDGROUPPRODUCTGROUPCODE,
       t.OTHERPRODUCTGROUPDEPBSRNO
FROM   DB2ADMIN.BENEFITSCHEMEMAP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
